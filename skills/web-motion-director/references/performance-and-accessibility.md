# Performance and accessibility

## Reduced motion

Respect `prefers-reduced-motion: reduce` for non-essential spatial motion. [R6]

SC 2.3.3 is Level AAA. Respecting reduced-motion preferences is also this skill's design standard; do not describe that specific criterion as an AA requirement or a complete accessibility check.

Do not merely reduce duration to almost zero while preserving large travel, zoom, parallax, or camera movement. Replace the effect with an equivalent state change.

Good substitutions:

- slide -> opacity or direct swap;
- parallax -> fixed layers;
- scrubbed spatial sequence -> ordinary document flow;
- route zoom -> short crossfade;
- 3D camera move -> static view;
- continuously rotating decoration -> static object.

## Continuous motion

WCAG 2.2 SC 2.2.2 is Level A. Its moving/blinking/scrolling branch requires a way to pause, stop, or hide qualifying information that begins automatically, lasts more than five seconds, and accompanies other content, unless essential. Its auto-updating branch has no five-second exception and also permits control of update frequency. Apply each branch's actual scope. Reduced-motion handling does not replace every required pause/update control. [R7]

A short asset played indefinitely creates long-running motion; apply the requirement to the resulting behavior, not just the source file length. Handle changes to the motion preference while an effect is running and leave a usable composed state.

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
