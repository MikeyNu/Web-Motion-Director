# Approved motion repair, 31 October 2026

The [desktop follow-up](../../VALIDATION-2026-10-31-DESKTOP.md) subsequently exercised this unchanged controller in local Edge, including keyboard, reversal, reduced motion, and layout. NOT RUN statements below describe the initial constrained exercise and remain historical evidence.

This is a retained fresh-context exercise, not a production-ready component or default motion recipe. Give a new evaluator only the neutral task below, [original fixture](index.html), actual capability limits, and the skill. Withhold the corrected source, checks, and this diagnosis until the output is complete.

## Task

Polish the Juniper notes disclosure: it feels slow and unreliable when opened and closed quickly. Preserve its approved copy, palette, layout, and rounded styling. Return corrected self-contained HTML with dependable, accessible behavior. Keep the input unchanged, use no packages or external assets, and report what was actually checked. Browser rendering is unavailable in this constrained exercise; do not use another preview route.

## Result and correction

[index.corrected.html](index.corrected.html) preserves the approved direction. The original relied on independent 1.2-second callbacks that could change semantics, visibility, or focus after a newer action. The repair updates disclosure state immediately, retargets optional 180 ms movement from the current sampled position, guards obsolete callbacks, supports reduced motion, and returns focus only when it is inside closing content. Page exit settles the latest state. The timing is a proposed implementation value, not playback-tuned evidence.

The original input remained unchanged. [Artifact hashes](artifact-hashes.json) identify the retained inputs, output, and check script. Run with Node.js:

```sh
node evals/qa-2026-10-31/verify.cjs
```

Fifteen checks pass using the actual inline controller with explicit fake DOM, animation, media-query, and timer objects. Coverage includes 1,000 rapid toggles, stale callbacks, reversals, conditional focus calls, Escape scope, live preference changes, absent/failed animation APIs, missing finish events, external cancellation, and page exit.

**NOT RUN:** browser layout, real keyboard/Tab/focus behavior, accessible-tree and assistive-technology behavior, normal-speed playback, temporal frames, actual history/cache restoration, zoom/reflow, and performance. A fake element's `focus()` call does not prove native focus behavior. No permitted browser preview was available; no alternate route was used. The source and logic result is useful but does not establish production readiness.

See the [package QA record](../../VALIDATION-2026-10-31-QA.md) and the companion's [five-case record](https://github.com/MikeyNu/agent-graphic-designer/blob/main/evals/validation-2026-10-31-qa.md).
