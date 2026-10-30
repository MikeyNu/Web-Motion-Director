"""Offline regression tests; fake browser objects do not establish browser QA."""
from contextlib import redirect_stdout
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "skills/web-motion-director/scripts"
sys.path.insert(0, str(SCRIPTS))
import motionctl
import browser_motion_audit as sampler


def plan():
    return {"version": 1, "project": "Queue", "motion_thesis": "Keep the selected record anchored.",
            "intents": [{"id": "detail", "posture": "spatial", "purpose": "Retain context",
                         "trigger": "Open record", "desktop": "Side inspector", "mobile": "Detail page",
                         "reduced_motion": "Direct swap"}]}


class TempCase(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path


class ScanTests(TempCase):
    def test_missing_and_empty_paths_cannot_look_clean(self):
        for path in (self.root / "missing", self.root):
            with self.subTest(path=path), self.assertRaises(ValueError):
                motionctl.scan(path)

    def test_skipped_sources_are_counted_and_reported(self):
        self.write("good.css", "body {color: black}")
        (self.root / "bad.css").write_bytes(b"\xff\xfe")
        result = motionctl.scan(self.root)
        self.assertEqual((result["files_found"], result["files_scanned"], result["files_skipped"]), (2, 1, 1))
        self.assertEqual(result["status"], "FAIL")

    def test_dependency_and_build_directories_are_excluded(self):
        self.write("app.css", "body {color: black}")
        for directory in ("node_modules", "dist", ".git"):
            self.write(f"{directory}/bad.css", "div {animation: spin 1s infinite}")
        result = motionctl.scan(self.root)
        self.assertEqual(result["files_scanned"], 1)
        self.assertEqual(result["findings"], [])
        self.assertEqual(result["status"], "REVIEW")

    def test_large_and_linked_sources_are_explicitly_uninspected(self):
        self.write("large.css", "x" * (motionctl.MAX_SOURCE_BYTES + 1))
        target = self.write("target.css", "body {}")
        (self.root / "link.css").symlink_to(target)
        result = motionctl.scan(self.root)
        self.assertEqual(result["files_skipped"], 2)
        self.assertEqual(result["status"], "FAIL")

    def test_motion_risks_remain_heuristics(self):
        path = self.write("app.css", "a {transition: all 1s; animation: spin 2s infinite; will-change: transform}")
        result = motionctl.scan(path)
        self.assertTrue({"WMD001", "WMD002", "WMD006", "WMD009"} <= {x["code"] for x in result["findings"]})
        self.assertIn("Heuristic", result["scope"])

    def test_multiple_scroll_owners_are_reported(self):
        path = self.write("app.js", "const a = new Lenis(); const b = ScrollSmoother.create();")
        self.assertIn("WMD008", {x["code"] for x in motionctl.scan(path)["findings"]})

    def test_cli_missing_path_is_json_with_nonzero_exit(self):
        output = io.StringIO()
        with redirect_stdout(output):
            code = motionctl.main(["scan", str(self.root / "missing"), "--json"])
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")


class PlanAndTagTests(TempCase):
    def test_valid_plan_and_deliberately_static_plan(self):
        self.assertEqual(motionctl.validate_plan_data(plan()), [])
        value = plan()
        value["intents"] = []
        value["motion_thesis"] = "Retain the approved static screen for this correction."
        self.assertEqual(motionctl.validate_plan_data(value), [])

    def test_null_empty_and_wrong_typed_fields_fail(self):
        self.assertTrue(motionctl.validate_plan_data(dict.fromkeys(plan())))
        for key in plan():
            for value in (None, False, " "):
                broken = plan()
                broken[key] = value
                with self.subTest(key=key, value=value):
                    self.assertTrue(motionctl.validate_plan_data(broken))

    def test_duplicate_ids_unknown_posture_and_empty_intent_fail(self):
        value = plan()
        value["intents"].append(copy.deepcopy(value["intents"][0]))
        self.assertTrue(motionctl.validate_plan_data(value))
        for key, bad in (("posture", "cinematic"), ("id", " "), ("mobile", {}), ("purpose", None)):
            value = plan()
            value["intents"][0][key] = bad
            self.assertTrue(motionctl.validate_plan_data(value))

    def test_tags_preserve_multiple_nested_objects_without_execution(self):
        path = self.write("index.html", '<!-- <motion-intent>{"id":"x","nested":{"a":2}}</motion-intent> -->\n<!-- <motion-intent>{"id":"y"}</motion-intent> -->')
        self.assertEqual(motionctl.extract_tags(path), [{"id": "x", "nested": {"a": 2}}, {"id": "y"}])

    def test_invalid_tags_are_not_silently_ignored(self):
        for text in ("[]", "null", '"text"', "", "{broken}"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                motionctl.extract_tags(self.write("index.html", f"<motion-intent>{text}</motion-intent>"))
        for text in ("<motion-intent>{}", "</motion-intent>", "<motion-intent><motion-intent>{}</motion-intent>"):
            with self.subTest(text=text), self.assertRaises(ValueError):
                motionctl.extract_tags(self.write("index.html", text))

    def test_no_tags_is_an_empty_result(self):
        self.assertEqual(motionctl.extract_tags(self.write("index.html", "<h1>Hello</h1>")), [])

    def test_malformed_json_cli_fails_cleanly(self):
        path = self.write("plan.json", "{broken}")
        output = io.StringIO()
        with redirect_stdout(output):
            code = motionctl.main(["validate-plan", str(path)])
        self.assertEqual(code, 2)
        self.assertIn("error", json.loads(output.getvalue()))


class FakePage:
    def __init__(self, failure=False):
        self.failure = failure
        self.events = {}
        self.y = 0
        self.extent_reads = 0
        self.screenshots = []
        self.navigation = None
        self.runtime_error = True
        self.http_status = None

    def on(self, name, callback):
        self.events[name] = callback

    def goto(self, url, **kwargs):
        self.navigation = (url, kwargs)
        if self.failure:
            raise RuntimeError("fixture navigation failure")
        if self.runtime_error:
            self.events["pageerror"]("fixture runtime exception")
        return types.SimpleNamespace(status=self.http_status) if self.http_status is not None else None

    def evaluate(self, expression, arg=None):
        if expression.startswith("Math.max"):
            self.extent_reads += 1
            return 1000 + 100 * self.extent_reads
        if expression.startswith("y =>"):
            self.y = max(0, arg - 17)  # Simulate an unsettled smooth scroll.
        elif expression == "window.scrollY":
            return self.y
        elif expression.startswith("document.getAnimations"):
            return 2
        elif expression.startswith("document.documentElement.scrollWidth"):
            return False

    def wait_for_timeout(self, ms):
        pass

    def screenshot(self, **kwargs):
        self.screenshots.append(kwargs)


class SamplerTests(TempCase):
    def test_actual_scroll_and_remeasured_extent_are_recorded(self):
        page = FakePage()
        rows = sampler.sample_page(page, self.root, "desktop", False)
        self.assertEqual(page.extent_reads, 5)
        self.assertEqual(rows[-1]["requested_scroll_y"], 1500)
        self.assertEqual(rows[-1]["scroll_y"], 1483)
        self.assertEqual(len(page.screenshots), 5)

    def fake_runtime(self, failure=False, runtime_error=True, http_status=None):
        contexts = []
        class Context:
            closed = False
            def __init__(self):
                self.page = FakePage(failure)
                self.page.runtime_error = runtime_error
                self.page.http_status = http_status
            def new_page(self):
                return self.page
            def close(self):
                self.closed = True
        class Browser:
            closed = False
            def new_context(self, **kwargs):
                context = Context()
                contexts.append(context)
                return context
            def close(self):
                self.closed = True
        browser = Browser()
        class Runtime:
            def __enter__(self):
                return types.SimpleNamespace(chromium=types.SimpleNamespace(launch=lambda **kwargs: browser))
            def __exit__(self, *args):
                pass
        module = types.ModuleType("playwright.sync_api")
        module.sync_playwright = Runtime
        return module, browser, contexts

    def test_navigation_keeps_file_base_and_records_runtime_errors(self):
        module, browser, contexts = self.fake_runtime()
        url = "file:///fixture/site/index.html"
        with patch.dict(sys.modules, {"playwright.sync_api": module}):
            report = sampler.audit(url, self.root)
        self.assertEqual(len(contexts), 6)
        self.assertTrue(browser.closed and all(c.closed for c in contexts))
        self.assertTrue(all(c.page.navigation[0] == url for c in contexts))
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["viewports"][0]["page_errors"], ["fixture runtime exception"])
        self.assertIn("Static scroll samples only", report["scope"])

    def test_navigation_failure_keeps_honest_report_and_closes_contexts(self):
        module, browser, contexts = self.fake_runtime(True)
        with patch.dict(sys.modules, {"playwright.sync_api": module}):
            report = sampler.audit("https://example.invalid/fixture", self.root)
        self.assertTrue(browser.closed and all(c.closed for c in contexts))
        self.assertTrue(all(run["status"] == "FAIL" and not run["samples"] for run in report["viewports"]))
        self.assertTrue((self.root / "motion-audit.json").exists())

    def test_http_error_page_is_not_reported_as_captured_product(self):
        module, browser, contexts = self.fake_runtime(runtime_error=False, http_status=500)
        with patch.dict(sys.modules, {"playwright.sync_api": module}):
            report = sampler.audit("https://example.invalid/fixture", self.root)
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(all("HTTP 500" in run["error"] and not run["samples"] for run in report["viewports"]))

    def test_successful_capture_does_not_claim_motion_pass(self):
        module, browser, contexts = self.fake_runtime(runtime_error=False, http_status=200)
        with patch.dict(sys.modules, {"playwright.sync_api": module}):
            report = sampler.audit("https://example.invalid/fixture", self.root)
        self.assertEqual(report["status"], "CAPTURED")
        self.assertEqual(sum(len(run["samples"]) for run in report["viewports"]), 30)
        self.assertNotIn('"PASS"', json.dumps(report))

    def test_old_evidence_is_not_overwritten(self):
        path = self.write("motion-audit.json", "original")
        with self.assertRaises(ValueError):
            sampler.audit("https://example.invalid/fixture", self.root)
        self.assertEqual(path.read_text(), "original")

    def test_invalid_scheme_is_rejected_before_runtime(self):
        with self.assertRaises(ValueError):
            sampler.audit("javascript:alert(1)", self.root)

    def test_missing_runtime_is_not_success(self):
        output = io.StringIO()
        with patch.dict(sys.modules, {"playwright.sync_api": None}), redirect_stdout(output):
            code = sampler.main(["https://example.invalid/fixture", "--out", str(self.root)])
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(output.getvalue())["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()
