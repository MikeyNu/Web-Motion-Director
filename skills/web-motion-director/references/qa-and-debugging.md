# Motion QA and debugging

## Motion is temporal

A resting screenshot proves only one state. Verify animation across time.

## Minimum temporal sample

For a non-trivial animation inspect:

1. before trigger;
2. immediately after trigger;
3. approximately 25 percent;
4. midpoint;
5. approximately 75 percent;
6. completion;
7. reverse or close;
8. interruption if the action can be interrupted.

For scroll-linked work, sample representative scroll positions instead of waiting fixed times.

## Visual craft and readiness

Inspect normal-speed playback before diagnosing individual frames. Check the onset, overlap, maximum occlusion, first readable state, input readiness, and final settlement. For masks and slices, inspect crop alignment, seams, fractional sizing, and resized states. For typography, check wrapping, font loading, glyph clipping, intermediate contrast, and duplicated accessible names. For shared objects, check subject/focal-point continuity and return geometry. For loops, inspect the ending-to-starting boundary and any intended velocity continuity.

Repeat the interaction several times. Check mid-flight reversal, a new selection, late data, skipped introduction, failed media, and a motion-preference change while active. Confirm the interface remains usable if an animation completion event never fires. Separate storyboard/specification review, sampled source evidence, rendered temporal QA, and actual performance measurement.

For a substantial new direction, compare choreography as well as effects: lead object, stable region, overlap, first readability, input readiness, repeat behavior, and end condition. Verify a principal expressive sequence and a frequent ordinary action. Check that demonstrated typing, numbers, progress, and completion are distinguishable from live state. Keep equivalent controls coherent; structural variety is not a quota for different animations. See [template choreography](graphic-design-coordination.md#prevent-template-choreography).

## Browser matrix

For substantial frontend implementation, select relevant conditions from this matrix. A narrow repair checks affected behavior and shared dependencies; a written specification records unexecuted runtime checks without expanding scope:

- narrow mobile;
- common mobile;
- tablet or narrow desktop;
- standard desktop;
- wide desktop when composition changes;
- reduced motion;
- keyboard-only interaction;
- direct route entry;
- back and forward navigation when transitions are route-based.

## Scroll QA

Check:

- section before animated range remains normal;
- entering range does not jump;
- pinned content does not cover focus or later content;
- progress maps correctly in both directions;
- horizontal distance ends exactly at intended edge;
- section unpins cleanly;
- page after animated range remains reachable;
- resize recomputes correctly;
- no unintended document-level horizontal scrollbar;
- deep links and anchor links still work.

## Navigation transition QA

Check:

- transition works from normal click;
- direct destination load works without transition state;
- back/forward works;
- leaving during a transition and returning restores a usable state, without stale guards, overlays, focus traps, or body locks;
- rapid second navigation does not leave overlay or body lock behind;
- focus lands in an appropriate destination location;
- route errors cannot leave the viewport covered;
- reduced motion bypasses spatial travel cleanly.

## Menu QA

Check:

- open;
- close;
- Escape;
- focus movement;
- focus return;
- rapid open/close interruption;
- viewport resize while open;
- route click while open;
- body scroll restored after teardown.

## Debugging common issues

### Trigger positions drift after images load

Measure after assets settle or refresh the scroll system at the correct lifecycle point. Reserve image dimensions.

### React page works once then duplicates effects

Look for missing effect cleanup, strict-mode double initialization, duplicated observers, or triggers recreated on each render.

### Horizontal section overshoots

Use measured `scrollWidth - clientWidth`, account for gaps/padding, and ensure transforms are applied to the intended track.

### Sticky or fixed elements break with smooth scrolling

Inspect whether a transformed scroll container changes the containing block. Verify the smooth-scroll library’s expected integration model.

### Animation snaps on reverse

Check from/to values, overwritten transforms, and whether the close animation incorrectly starts from an assumed final state rather than the current rendered state.

### Reduced motion still moves

Search both CSS and JavaScript. A CSS media query does not automatically disable JS timelines.

## Evidence language

Use:

- `PASS`: checked and satisfied.
- `FAIL`: checked and did not satisfy.
- `NOT RUN`: relevant but not executed.
- `N/A`: genuinely outside scope, with a reason.

Attach `blocked` and its concrete reason to a NOT RUN check when a capability prevents execution. Keep stage (specified, prototyped, integrated) separate from these results. A prototype can pass a local interaction check without demonstrating a backend operation. Isolated logic tests with fake DOM or browser objects validate only the tested logic and helper contract; they do not replace browser interaction, layout, or timing checks.

For retained-page behavior, record whether a real back/forward cache restoration occurred. Dispatching `pagehide`/`pageshow` or navigating Back in an automation tool does not establish that. Check the tool's current support; the [31 October research note](../RESEARCH.md#31-october-2026-qa-and-lifecycle-refresh) records a relevant Playwright limitation.

The optional [browser sampler](../scripts/README.md) captures static scroll positions. Its normal/reduced contexts do not prove that the two experiences differ appropriately, and its running-animation count is not a frame-rate measurement. Inspect the images and actual sequences separately. Follow host tool policies; an unavailable or blocked runtime is a limitation to report, not permission to bypass it.

Do not write “motion verified” when only typecheck or build ran.

Validate unexpected test failures before changing the UI. Native browser controls can receive focus outside the document; distinguish that from a background-page control becoming focusable through an open modal. Preserve failure evidence and document any corrected harness assumption. Capture viewport images for fixed overlays because a full-page composite can misrepresent what is simultaneously visible. Numeric motion traces supplement visual inspection; they do not alone certify perceived smoothness or device performance.
