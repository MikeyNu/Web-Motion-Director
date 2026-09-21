#!/usr/bin/env python3
"""Conservative static helper for Web Motion Director."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TEXT_SUFFIXES = {".css", ".scss", ".sass", ".less", ".js", ".jsx", ".ts", ".tsx", ".html", ".vue", ".svelte"}
SKIP_DIRS = {".git", "node_modules", ".next", "dist", "build", "out", "coverage", ".turbo", ".cache", "vendor"}


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
    findings = []
    files = list(iter_source_files(root))
    joined = []
    motion = False
    engines = set()

    def add(code: str, path: Path, message: str, severity: str = "warning"):
        findings.append({"code": code, "severity": severity, "path": str(path), "message": message})

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        joined.append(text)
        if re.search(r"transition\s*:|@keyframes|animation\s*:|gsap\.|ScrollTrigger|motion\.|animate\(|startViewTransition|scroll-timeline|animation-timeline", text, re.I):
            motion = True
        if re.search(r"transition\s*:\s*all\b", text, re.I):
            add("WMD002", path, "Avoid transition: all; declare the intended animated properties.")
        if re.search(r"animation[^;\n]*\binfinite\b|repeat\s*:\s*-1|repeat\s*:\s*Infinity", text, re.I):
            add("WMD006", path, "Infinite animation detected. Confirm continuous motion is necessary and controllable.")
        if re.search(r"addEventListener\s*\(\s*['\"]scroll['\"]", text, re.I) and not re.search(r"requestAnimationFrame|ScrollTrigger|Lenis", text, re.I):
            add("WMD004", path, "Raw scroll listener detected without an obvious scheduling or scroll system nearby.")
        if re.search(r"addEventListener\s*\(\s*['\"](?:wheel|touchmove)['\"]", text, re.I) and "preventDefault" in text:
            add("WMD005", path, "Wheel or touch handler calls preventDefault. Confirm native scrolling remains usable.")
        if "will-change:" in text:
            add("WMD009", path, "Persistent will-change detected. Review memory and compositing cost.")
        if re.search(r"\bLenis\b", text): engines.add("lenis")
        if re.search(r"ScrollSmoother", text): engines.add("scrollsmoother")
        if re.search(r"LocomotiveScroll|locomotive-scroll", text, re.I): engines.add("locomotive")

    all_text = "\n".join(joined)
    if motion and not re.search(r"prefers-reduced-motion|matchMedia\s*\([^)]*reduceMotion|reducedMotion\s*:", all_text, re.I):
        add("WMD001", root, "Motion detected but no reduced-motion handling was found in the scanned source set.", "error")
    if len(engines) > 1:
        add("WMD008", root, f"Multiple smooth-scroll engines detected: {', '.join(sorted(engines))}.", "error")

    return {"root": str(root), "files_scanned": len(files), "motion_detected": motion, "smooth_scroll_engines": sorted(engines), "findings": findings}


def extract_tags(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    tags = []
    for match in re.finditer(r"<motion-intent>\s*(\{.*?\})\s*</motion-intent>", text, re.S | re.I):
        value = json.loads(match.group(1))
        if not isinstance(value, dict):
            raise ValueError("motion-intent JSON must be an object")
        tags.append(value)
    return tags


def validate_plan_data(data: object) -> list[str]:
    errors = []
    if not isinstance(data, dict):
        return ["Plan root must be an object."]
    for key in ("version", "project", "motion_thesis", "intents"):
        if key not in data:
            errors.append(f"Missing required field: {key}")
    intents = data.get("intents")
    if intents is not None and not isinstance(intents, list):
        errors.append("intenÛm}r«²ÚîÆ­y