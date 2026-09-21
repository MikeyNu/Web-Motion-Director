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

## Browser matrix

At minimum for substantial frontend motion:

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
- `BLOCKED`: could not verify because of a concrete limitation.
- `NOT RUN`: relevant but not executed.
- `NOT APPLICABLE`: genuinely outside scope.

Do not write “motion verified” when only typecheck or build ran.
