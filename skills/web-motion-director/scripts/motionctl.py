#!/usr/bin/env python3
"""Conservative static helper for Web Motion Director."""
from __future__ import annotations

import argparse
import json
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


def iter_source_files(root: Path):
    if root.is_file():
        if root.suffix.lower() in TEXT_SUFFIXES:
            yield root
        return

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            rel = path.relative_to(root)
        except ValueError:
            rel = path
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        yield path


def scan(root: Path) -> dict:
    findings: list[dict] = []
    files = list(iter_source_files(root))
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
            source = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

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
        "root": str(root),
        "files_scanned": len(files),
        "motion_detected": motion,
        "smooth_scroll_engines": sorted(engines),
        "findings": findings,
    }


def extract_tags(path: Path) -> list[dict]:
    source = path.read_text(encoding="utf-8")
    tags: list[dict] = []
    pattern = r"<motion-intent>\s*(\{.*?\})\s*</motion-intent>"
    for match in re.finditer(pattern, source, re.S | re.I):
        value = json.loads(match.group(1))
        if not isinstance(value, dict):
            raise ValueError("motion-intent JSON must be an object")
        tags.append(value)
    return tags


def validate_plan_data(data: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Plan root must be an object."]

    for key in ("version", "project", "motion_thesis", "intents"):
        if key not in data:
            errors.append(f"Missing required field: {key}")

    intents = data.get("intents")
    if intents is not None and not isinstance(intents, list):
        errors.append("intents must be an array.")
        return errors

    if isinstance(intents, list):
        for index, intent in enumerate(intents):
            if not isinstance(intent, dict):
                errors.append(f"intents[{index}] must be an object.")
                continue
            for key in (
                "id",
                "posture",
                "purpose",
                "trigger",
                "desktop",
                "mobile",
                "reduced_motion",
            ):
                if key not in intent:
                    errors.append(f"intents[{index}] missing required field: {key}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(prog="motionctl")
    sub = parser.add_subparsers(dest="command", required=True)

    scan_parser = sub.add_parser("scan", help="Scan frontend source for motion risks.")
    scan_parser.add_argument("path")
    scan_parser.add_argument("--json", action="store_true")

    tags_parser = sub.add_parser("extract-tags", help="Extract inert motion-intent JSON blocks.")
    tags_parser.add_argument("path")

    plan_parser = sub.add_parser("validate-plan", help="Validate the basic motion-plan structure.")
    plan_parser.add_argument("path")

    args = parser.parse_args()

    if args.command == "scan":
        result = scan(Path(args.path))
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"files_scanned={result['files_scanned']}")
            print(f"motion_detected={str(result['motion_detected']).lower()}")
            for finding in result["findings"]:
                print(
                    f"{finding['severity'].upper()} {finding['code']} "
                    f"{finding['path']}: {finding['message']}"
                )
        return 1 if any(item["severity"] == "error" for item in result["findings"]) else 0

    if args.command == "extract-tags":
        print(json.dumps(extract_tags(Path(args.path)), indent=2))
        return 0

    if args.command == "validate-plan":
        data = json.loads(Path(args.path).read_text(encoding="utf-8"))
        errors = validate_plan_data(data)
        print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
        return 0 if not errors else 1

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
