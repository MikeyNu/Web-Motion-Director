#!/usr/bin/env python3
"""Conservative static helper for Web Motion Director."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path

TEXT_SUFFIXES = {
    ".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts", ".tsx",
    ".html", ".vue", ".svelte",
}
SKIP_DIRS = {
    ".git", "node_modules", ".next", "dist", "build", "out", "coverage",
    ".turbo", ".cache", "vendor",
}
POSTURES = {"static", "feedback", "spatial", "scroll-linked", "narrative", "immersive"}
MAX_SOURCE_BYTES = 2 * 1024 * 1024
SCOPE = "Heuristic source inspection only; no rendered, temporal, accessibility, or performance verification."


def iter_source_files(root: Path):
    if not root.exists():
        raise ValueError(f"Scan path does not exist: {root}")
    if root.is_file():
        if root.suffix.lower() in TEXT_SUFFIXES:
            yield root
        return

    def fail(error):
        raise error

    for directory, names, files in os.walk(root, followlinks=False, onerror=fail):
        names[:] = sorted(name for name in names if name not in SKIP_DIRS)
        for name in sorted(files):
            path = Path(directory) / name
            if path.suffix.lower() in TEXT_SUFFIXES:
                yield path


def scan(root: Path) -> dict:
    findings: list[dict] = []
    files = list(iter_source_files(root))
    if not files:
        raise ValueError("No supported frontend source files found; no scan was performed.")
    scanned = 0
    joined: list[str] = []
    motion = False
    engines: set[str] = set()

    def add(code: str, path: Path, message: str, severity: str = "warning") -> None:
        findings.append({
            "code": code,
            "severity": severity,
            "path": str(path),
            "message": message,
        })

    for path in files:
        try:
            if path.is_symlink():
                raise ValueError("Symbolic-link source was not followed.")
            with path.open("rb") as stream:
                raw = stream.read(MAX_SOURCE_BYTES + 1)
            if len(raw) > MAX_SOURCE_BYTES:
                raise ValueError("Source exceeds the 2 MiB per-file inspection limit.")
            source = raw.decode("utf-8-sig")
        except (OSError, UnicodeError, ValueError) as error:
            add("WMD000", path, f"Source not inspected: {error}", "error")
            continue
        scanned += 1
        joined.append(source)

        if re.search(
            r"transition\s*:|@keyframes|animation\s*:|gsap\.|ScrollTrigger|"
            r"motion\.|animate\(|startViewTransition|scroll-timeline|animation-timeline",
            source,
            re.I,
        ):
            motion = True

        if re.search(r"transition\s*:\s*all\b", source, re.I):
            add("WMD002", path, "Avoid transition: all; declare the intended animated properties.")

        if re.search(
            r"animation[^;\n]*\binfinite\b|repeat\s*:\s*-1|repeat\s*:\s*Infinity",
            source,
            re.I,
        ):
            add(
                "WMD006",
                path,
                "Infinite animation detected. Confirm continuous motion is necessary and controllable.",
            )

        if re.search(r"addEventListener\s*\(\s*['\"]scroll['\"]", source, re.I) and not re.search(
            r"requestAnimationFrame|ScrollTrigger|Lenis", source, re.I
        ):
            add(
                "WMD004",
                path,
                "Raw scroll listener detected without an obvious scheduling or scroll system nearby.",
            )

        if re.search(
            r"addEventListener\s*\(\s*['\"](?:wheel|touchmove)['\"]", source, re.I
        ) and "preventDefault" in source:
            add(
                "WMD005",
                path,
                "Wheel or touch handler calls preventDefault. Confirm native scrolling remains usable.",
            )

        if "will-change:" in source:
            add(
                "WMD009",
                path,
                "Persistent will-change detected. Review memory and compositing cost.",
            )

        if re.search(r"\bLenis\b", source):
            engines.add("lenis")
        if re.search(r"ScrollSmoother", source):
            engines.add("scrollsmoother")
        if re.search(r"LocomotiveScroll|locomotive-scroll", source, re.I):
            engines.add("locomotive")

    all_text = "\n".join(joined)
    reduced_motion_pattern = (
        r"prefers-reduced-motion|matchMedia\s*\([^)]*reduceMotion|reducedMotion\s*:"
    )
    if motion and not re.search(reduced_motion_pattern, all_text, re.I):
        add(
            "WMD001",
            root,
            "Motion detected but no reduced-motion handling was found in the scanned source set.",
            "error",
        )

    if len(engines) > 1:
        add(
            "WMD008",
            root,
            f"Multiple smooth-scroll engines detected: {', '.join(sorted(engines))}.",
            "error",
        )

    return {
        "status": "FAIL" if any(item["severity"] == "error" for item in findings) else "REVIEW",
        "scope": SCOPE,
        "root": str(root),
        "files_found": len(files),
        "files_scanned": scanned,
        "files_skipped": len(files) - scanned,
        "motion_detected": motion,
        "smooth_scroll_engines": sorted(engines),
        "findings": findings,
    }


def extract_tags(path: Path) -> list[dict]:
    source = path.read_text(encoding="utf-8")
    tags: list[dict] = []
    opening = None
    for match in re.finditer(r"</?motion-intent>", source, re.I):
        if not match.group().startswith("</"):
            if opening is not None:
                raise ValueError("Nested motion-intent tags are not supported.")
            opening = match.end()
        else:
            if opening is None:
                raise ValueError("Closing motion-intent tag has no opening tag.")
            value = json.loads(source[opening:match.start()])
            if not isinstance(value, dict):
                raise ValueError("motion-intent JSON must be an object")
            tags.append(value)
            opening = None
    if opening is not None:
        raise ValueError("Unclosed motion-intent tag.")
    return tags


def validate_plan_data(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Plan root must be an object."]

    version = data.get("version")
    if not ((isinstance(version, str) and version.strip()) or (type(version) is int and version > 0)):
        errors.append("version must be a nonempty string or positive integer.")
    if not isinstance(data.get("project"), str) or not data["project"].strip():
        errors.append("project must be a nonempty string.")

    def description(value):
        return (isinstance(value, str) and bool(value.strip())) or (isinstance(value, dict) and bool(value))

    if not description(data.get("motion_thesis")):
        errors.append("motion_thesis must be nonempty text or an object describing the direction.")

    intents = data.get("intents")
    if not isinstance(intents, list):
        errors.append("intents must be an array.")
        return errors

    if isinstance(intents, list):
        identifiers = set()
        for index, intent in enumerate(intents):
            if not isinstance(intent, dict):
                errors.append(f"intents[{index}] must be an object.")
                continue
            identifier = intent.get("id")
            if not isinstance(identifier, str) or not identifier.strip():
                errors.append(f"intents[{index}].id must be a nonempty string.")
            elif identifier.strip() in identifiers:
                errors.append(f"Duplicate intent id: {identifier.strip()}")
            else:
                identifiers.add(identifier.strip())
            if not isinstance(intent.get("posture"), str) or intent["posture"] not in POSTURES:
                errors.append(f"intents[{index}].posture must be one of {', '.join(sorted(POSTURES))}.")
            for key in (
                "purpose",
                "trigger",
                "desktop",
                "mobile",
                "reduced_motion",
            ):
                if not description(intent.get(key)):
                    errors.append(f"intents[{index}].{key} must be nonempty text or an object.")

    return errors


class JsonArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(json.dumps({"status": "FAIL", "error": message, "scope": SCOPE}))
        raise SystemExit(2)


def run(args) -> int:
    if args.command == "scan":
        result = scan(Path(args.path))
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"files_scanned={result['files_scanned']} files_skipped={result['files_skipped']}")
            print(f"motion_detected={str(result['motion_detected']).lower()}")
            print(SCOPE)
            for finding in result["findings"]:
                print(f"{finding['severity'].upper()} {finding['code']} {finding['path']}: {finding['message']}")
        return 1 if result["status"] == "FAIL" else 0
    if args.command == "extract-tags":
        print(json.dumps(extract_tags(Path(args.path)), indent=2))
        return 0
    data = json.loads(Path(args.path).read_text(encoding="utf-8"))
    errors = validate_plan_data(data)
    print(json.dumps({"valid": not errors, "errors": errors, "scope": "Structure only; content, completeness, and behavior require review."}, indent=2))
    return 1 if errors else 0


def main(argv=None) -> int:
    parser = JsonArgumentParser(prog="motionctl")
    sub = parser.add_subparsers(dest="command", required=True)

    scan_parser = sub.add_parser("scan", help="Scan frontend source for motion risks.")
    scan_parser.add_argument("path")
    scan_parser.add_argument("--json", action="store_true")

    tags_parser = sub.add_parser("extract-tags", help="Extract inert motion-intent JSON blocks.")
    tags_parser.add_argument("path")

    plan_parser = sub.add_parser("validate-plan", help="Validate the basic motion-plan structure.")
    plan_parser.add_argument("path")

    args = parser.parse_args(argv)
    try:
        return run(args)
    except (OSError, UnicodeError, ValueError, RuntimeError) as error:
        print(json.dumps({"status": "FAIL", "error": str(error), "scope": SCOPE}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
