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
from urllib.parse import urlparse

VIEWPORTS = [
    ("mobile", 390, 844),
    ("tablet", 768, 1024),
    ("desktop", 1440, 1000),
]
SCROLL_SAMPLES = [0.0, 0.25, 0.5, 0.75, 1.0]
SCOPE = "Static scroll samples only. No normal-speed playback, interaction, accessibility conformance, or performance verification."


def sample_page(page, out: Path, label: str, reduced: bool) -> list[dict]:
    samples = []
    for fraction in SCROLL_SAMPLES:
        # Content may grow after earlier samples trigger lazy loading.
        max_scroll = page.evaluate("Math.max(0, document.documentElement.scrollHeight - innerHeight)")
        requested_y = int(max_scroll * fraction)
        page.evaluate("y => window.scrollTo(0, y)", requested_y)
        page.wait_for_timeout(250)
        actual_y = page.evaluate("window.scrollY")
        active = page.evaluate("document.getAnimations().filter(a => a.playState === 'running').length")
        overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth + 1")
        name = f"{label}-{'reduced' if reduced else 'normal'}-{int(fraction*100):03d}.png"
        page.screenshot(path=str(out / name), full_page=False)
        samples.append({"fraction": fraction, "requested_scroll_y": requested_y, "scroll_y": actual_y,
                        "measured_max_scroll": max_scroll, "active_animations": active,
                        "horizontal_overflow": overflow, "screenshot": name})
    return samples


def audit(url: str, out: Path, headed: bool = False) -> dict:
    if urlparse(url).scheme not in {"http", "https", "file"}:
        raise ValueError("Use an http, https, or file URL supported and authorized by your host.")
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise ValueError("Output must be a new or empty directory; previous evidence is not overwritten.")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("Playwright is not installed. See requirements-optional.txt") from exc

    out.mkdir(parents=True, exist_ok=True)
    report = {"url": url, "scope": SCOPE, "status": "NOT RUN", "viewports": []}
    with sync_playwright() as p:
        launch_args = {"headless": not headed}
        override = os.environ.get("WMD_CHROMIUM")
        system_chromium = override or shutil.which("chromium") or shutil.which("chromium-browser") or shutil.which("google-chrome")
        if system_chromium:
            launch_args["executable_path"] = system_chromium
        browser = p.chromium.launch(**launch_args)
        try:
            for label, width, height in VIEWPORTS:
                for reduced in (False, True):
                    context = browser.new_context(
                        viewport={"width": width, "height": height},
                        reduced_motion="reduce" if reduced else "no-preference",
                    )
                    run = {"label": label, "width": width, "height": height, "reduced_motion": reduced,
                           "console_errors": [], "page_errors": [], "samples": [], "status": "NOT RUN"}
                    report["viewports"].append(run)
                    try:
                        page = context.new_page()
                        page.on("console", lambda msg, errors=run["console_errors"]: errors.append(msg.text) if msg.type == "error" else None)
                        page.on("pageerror", lambda error, errors=run["page_errors"]: errors.append(str(error)))
                        # Keep the document URL and relative asset base intact, including file URLs.
                        response = page.goto(url, wait_until="load", timeout=30000)
                        if response is not None and response.status >= 400:
                            raise RuntimeError(f"Navigation returned HTTP {response.status}.")
                        run["samples"] = sample_page(page, out, label, reduced)
                        run["status"] = "CAPTURED"
                    except Exception as error:
                        run["status"] = "FAIL"
                        run["error"] = f"{type(error).__name__}: {error}"
                    finally:
                        context.close()
        finally:
            browser.close()
    report["status"] = "FAIL" if any(run["status"] == "FAIL" or run["console_errors"] or run["page_errors"] or
                                                any(sample["horizontal_overflow"] for sample in run["samples"])
                                                for run in report["viewports"]) else "CAPTURED"
    (out / "motion-audit.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return report


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--out", default="motion-audit")
    ap.add_argument("--headed", action="store_true")
    args = ap.parse_args(argv)
    try:
        report = audit(args.url, Path(args.out), args.headed)
    except Exception as error:
        print(json.dumps({"status": "FAIL", "error": f"{type(error).__name__}: {error}", "scope": SCOPE}))
        return 2
    print(json.dumps({"url": report["url"], "status": report["status"], "scope": SCOPE,
                      "runs": len(report["viewports"]), "output": str(Path(args.out).resolve())}, indent=2))
    return 1 if report["status"] == "FAIL" else 0

if __name__ == "__main__":
    raise SystemExit(main())
