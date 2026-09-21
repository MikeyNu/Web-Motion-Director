#!/usr/bin/env python3
"""Diagnostic browser sampler for motion-heavy pages.

Requires: pip install playwright && playwright install chromium
This helper captures static samples at multiple scroll positions. It does not
replace a human or model review of the actual animation.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
from pathlib import Path
from urllib.parse import unquote, urlparse

VIEWPORTS = [
    ("mobile", 390, 844),
    ("tablet", 768, 1024),
    ("desktop", 1440, 1000),
]
SCROLL_SAMPLES = [0.0, 0.25, 0.5, 0.75, 1.0]


def audit(url: str, out: Path, headed: bool = False) -> dict:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit("Playwright is not installed. See requirements-optional.txt") from exc

    out.mkdir(parents=True, exist_ok=True)
    report = {"url": url, "viewports": []}
    with sync_playwright() as p:
        launch_args = {"headless": not headed}
        override = os.environ.get("WMD_CHROMIUM")
        system_chromium = override or shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")
        if system_chromium:
            launch_args["executable_path"] = system_chromium
        browser = p.chromium.launch(**launch_args)
        for label, width, height in VIEWPORTS:
            for reduced in (False, True):
                context = browser.new_context(
                    viewport={"width": width, "height": height},
                    reduced_motion="reduce" if reduced else "no-preference",
                )
                page = context.new_page()
                errors = []
                page.on("console", lambda msg, errors=errors: errors.append(msg.text) if msg.type == "error" else None)
                if url.startswith("file://"):
                    local_path = Path(unquote(urlparse(url).path))
                    page.set_content(local_path.read_text(encoding="utf-8"), wait_until="load")
                else:
                    page.goto(url, wait_until="networkidle")
                max_scroll = page.evaluate("Math.max(0, document.documentElement.scrollHeight - innerHeight)")
                samples = []
                for fraction in SCROLL_SAMPLES:
                    y = int(max_scroll * fraction)
                    page.evaluate("y => window.scrollTo(0, y)", y)
                    page.wait_for_timeout(250)
                    active = page.evaluate("document.getAnimations().filter(a => a.playState === 'running').length")
                    overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth + 1")
                    name = f"{label}-{'reduced' if reduced else 'normal'}-{int(fraction*100):03d}.png"
                    page.screenshot(path=str(out / name), full_page=False)
                    samples.append({"fraction": fraction, "scroll_y": y, "active_animations": active, "horizontal_overflow": overflow, "screenshot": name})
                report["viewports"].append({
                    "label": label,
                    "width": width,
                    "height": height,
                    "reduced_motion": reduced,
                    "console_errors": errors,
                    "samples": samples,
                })
                context.close()
        browser.close()
    (out / "motion-audit.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", default="motion-audit")
    ap.add_argument("--headed", action="store_true")
    args = ap.parse_args()
    report = audit(args.url, Path(args.out), args.headed)
    print(json.dumps({"url": report["url"], "runs": len(report["viewports"]), "output": str(Path(args.out).resolve())}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
