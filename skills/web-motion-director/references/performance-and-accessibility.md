# Performance and accessibility

## Reduced motion

Respect `prefers-reduced-motion: reduce` for non-essential spatial motion. [R6]

Do not merely reduce duration to almost zero while preserving large travel, zoom, parallax, or camera movement. Replace the effect with an equivalent state change.

Good substitutions:

- slide -> opacity or direct swap;
- parallax -> fixed layers;
- scrubbed spatial sequence -> ordinary document flow;
- route zoom -> short crossfade;
- 3D camera move -> static view;
- continuously rotating decoration -> static object.

## Continuous motion

WCAG guidance requires controls for moving, blinking, scrolling, or auto-updating content that starts automatically, lasts longer than five seconds, and runs in parallel with other content unless it is essential. [R7]

Examples to review carefully:

- logo marquees;
- auto-scrolling testimonials;
- carousels;
- animated backgrounds;
- looping hero reels;
- stock tickers;
- perpetual decorative 3D scenes.

## Flashing

Avoid content that can violate seizure and physical-reaction guidance. Do not use rapid high-contrast flashes as a transition motif.

## Keyboard and focus

Motion must not change focus order or hide the currently focused element.

Check:

- menu open/close;
- dialogs and drawers;
- route transitions;
- carousels and horizontal rails;
- pinned sections;
- transformed content;
- back/forward navigation.

A visual element moving away does not justify moving keyboard focus unexpectedly.

## Pointer-only motion

Hover can enhance but cannot be the only way to discover required information or action. Provide focus equivalents for keyboard users and meaningful behavior for touch devices.

## Performance pipeline

Prefer `transform` and `opacity` where practical because they can remain in the compositing stage. Profile layout and paint when animating other properties. [R5]

Avoid:

- layout reads followed by writes in repeated loops;
- per-frame updates through React state for purely visual changes;
- continuous large blur/filter animation;
- many simultaneous box-shadow animations;
- hundreds of independent scroll listeners;
- permanent `will-change` on large groups;
- uncontrolled RAF loops after route changes;
- full-resolution WebGL on all devices.

## Image and media loading

Motion should not cause layout shift when media arrives. Reserve dimensions. When a transition depends on an image, ensure the relevant media is ready or provide a stable fallback state rather than jumping into the animation with missing dimensions.

## Performance verification

For substantial motion:

1. inspect in the browser on representative desktop and mobile viewports;
2. watch for visible dropped frames and long tasks;
3. check console warnings/errors;
4. inspect layout shifts and overflow;
5. profile if the motion is janky or expensive;
6. test with CPU/GPU constraints when the experience is graphics-heavy;
7. verify cleanup by navigating away and back repeatedly.

Do not declare 60 FPS unless it was measured in an appropriate environment.

## Progressive enhancement

Critical content and navigation should remain accessible if an animation library fails to load. Heavy brand motion can enhance the experience, but it should not become the only representation of essential content.
