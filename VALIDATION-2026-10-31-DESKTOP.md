# Local desktop browser follow-up, 31 October 2026

The user authorized the local desktop browser and confirmed that GitHub CI is unavailable due to billing. The initial cloud-browser limitation no longer prevents the explicitly authorized desktop run.

The [full joint record](https://github.com/MikeyNu/agent-graphic-designer/blob/main/evals/validation-2026-10-31-desktop.md) and [reproducible runner/evidence](https://github.com/MikeyNu/agent-graphic-designer/tree/main/evals/browser-qa) document 39 passing browser checks in headed local Edge 156.0.4314.50, across five viewport sizes in normal/reduced motion. Thirty axe scans reported no selected-rule violations; incomplete/manual checks remain distinct.

The unchanged Juniper controller passed native Enter/Tab/Escape behavior, focus return, actual rapid pointer activation, live reduced-motion changes, viewport changes, large-text/spacing stress, and the JavaScript-disabled fallback. Browser animation-frame samples record actual normal/reduced sequences. Source-level assertions were not substituted for this run. Canonical source hash: `2860c33e1aa2daff9f595b9295e3c2fb4b4d675491da7b2f13c64cc63d761fc3`.

The companion queue needed rendered-contrast and responsive-layout repairs. All 39 checks then passed. A separate standalone Edge test, without Playwright/CDP, observed real `pagehide.persisted` and `pageshow.persisted` restoration during close. It verified settled dialog state, unlocked body scrolling, restored record focus, and subsequent reopen/close. This is one genuine BFCache case on the named browser, not a synthetic lifecycle test or cross-browser certification.

The test harness also needed correction: native browser-control focus is distinct from background-page focus, text resizing must capture baselines before mutation, and fixed-overlay captures should use the viewport. These lessons refine the QA guide without imposing a new animation style.

Limits: desktop-sized mobile viewports do not test real phones; axe is not complete accessibility conformance; native zoom, screen readers, OS-level preference switching, other engines, and production integration remain untested. Videos were recorded, but continuous visual playback was not independently watched; inspected captures and actual temporal traces support bounded sequence claims, not perceived smoothness or measured performance. GitHub CI remains unavailable due to billing; local package checks remain the automated package evidence.
