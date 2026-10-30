# Helpers and their evidence limits

Use Python 3.10 or newer. `motionctl.py` uses only the standard library and does not rewrite project files. The browser sampler is optional and requires an installed Playwright/browser runtime plus host authorization to use it. Neither script installs dependencies. Use the host's permitted browser tools when required; these helpers are never a workaround for a policy block.

Commands below run from this skill directory. Replace example input/output paths with the actual project paths.

## Static source inspection

```bash
python scripts/motionctl.py scan path/to/frontend --json
python scripts/motionctl.py extract-tags path/to/component.html
python scripts/motionctl.py validate-plan path/to/motion-plan.json
```

The scanner prunes dependency/build folders, inspects supported frontend text files up to 2 MiB each, and reports found, inspected, and skipped counts. Missing paths, no supported sources, unreadable files, oversized files, and symbolic-link files cannot masquerade as a clean scan. It does not follow symbolic-link directories. The rules are regular-expression heuristics: comments and strings can produce false positives, and indirect/generated implementation can be missed. Finding a reduced-motion token does not prove appropriate behavior. No findings means REVIEW, never motion verified.

Tag extraction accepts JSON objects between literal `<motion-intent>` and `</motion-intent>` delimiters. It reads data without executing it. Non-object JSON, invalid JSON, nested tags, and unmatched delimiters are errors, not absent tags. A file with no tags returns an empty list. Tags do not authorize work and cannot override the task or repository instructions.

## Plan structure

```json
{
  "version": 1,
  "project": "Reservation queue",
  "motion_thesis": "Keep the selected record stable while opening its detail.",
  "intents": [{
    "id": "record-detail",
    "posture": "spatial",
    "purpose": "Retain the relationship to the queue",
    "trigger": "Open a reservation",
    "desktop": "Side inspector with the queue stationary",
    "mobile": "Focused detail view with return context",
    "reduced_motion": "Direct state swap with the same information"
  }]
}
```

`version` is a nonempty string or positive integer; `project` is nonempty text. `motion_thesis`, `purpose`, `trigger`, `desktop`, `mobile`, and `reduced_motion` accept nonempty text or a nonempty object. Intent IDs must be nonempty and unique. Posture is `static`, `feedback`, `spatial`, `scroll-linked`, `narrative`, or `immersive`. Additional fields are allowed for the shared contract. An empty intents array is valid for a deliberate static outcome explained in the thesis. Structure validation does not judge the descriptions, identify omitted states, or prove any behavior.

## Browser scroll samples

```bash
python scripts/browser_motion_audit.py https://your-authorized-preview.example --out path/to/new-audit
```

Run only against an authorized review target. The helper visits it in six contexts: mobile, tablet, desktop, each with normal and reduced motion. Each captures five scroll fractions after a fixed 250 ms wait. It does not click controls, submit forms, capture continuous playback, wait for all application data, or establish font readiness. For permitted local file URLs, ordinary navigation preserves relative asset resolution; loading file bytes into a blank page would not.

The output must be a new or empty directory, preserving previous evidence. The JSON records requested and actual scroll positions, the currently measured scroll extent, running-animation count, document overflow, console errors, runtime exceptions, and capture failures. Layout growth or smooth scrolling can make the actual position differ; inspect this evidence instead of treating a requested fraction as a verified temporal state. A count of running animations does not measure FPS.

`CAPTURED` means screenshots were captured without the listed detected errors. It is not PASS for motion design, reduced-motion quality, keyboard access, route behavior, performance, or accessibility. A detected failure keeps a partial report where possible. Missing dependencies or a failed browser launch produce an explicit error, not verification.

| Command | Exit 0 | Exit 1 | Exit 2 |
| --- | --- | --- | --- |
| Source scan | Completed without error-level findings; review still required | Error-level finding or uninspected source | Invalid/missing input or no supported files |
| Tags | Objects extracted, or no tags present | Not used | Invalid input/tag or unreadable file |
| Plan | Basic structure accepted | Invalid plan structure | Invalid invocation, unreadable file, or invalid JSON |
| Browser sampler | Static captures completed without detected errors | Capture, console, runtime, or document-overflow issue | Invalid input, missing runtime, or launch/output failure |

Run offline regression tests from the repository root with `python3 -m unittest discover -s tests -v`. Tests using fake browser objects validate helper behavior only; actual rendered review remains a separate task.
