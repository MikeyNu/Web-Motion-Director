# Responsive motion

## Principle

Responsive motion is art direction. The relationship between content, input, viewport, and motion changes across devices.

## Breakpoint questions

For every major motion system ask:

- Is the same effect still useful on a narrow screen?
- Does the movement consume too much vertical space?
- Does pinning trap too much of the viewport?
- Is the input pointer-dependent?
- Does the user need direct touch control instead?
- Is the text still readable while movement happens?
- Is a horizontal sequence still discoverable?
- Can the device afford the graphical work?

## Common transformations

### Desktop pinned horizontal -> mobile vertical

Use when cards or chapters that fit a cinematic desktop treatment need straightforward mobile reading.

### Desktop scrub -> mobile discrete state

Instead of continuously scrubbing a complex effect, move between a few clear states as sections enter.

### Pointer parallax -> touch static

Do not simulate pointer parallax from device motion unless that is explicitly part of the product and permission model.

### WebGL -> lighter canvas or image sequence

Reduce scene complexity, device pixel ratio, post-processing, shadow quality, particle counts, or replace the scene with static art.

### Large shared-element zoom -> short continuity fade

A full-screen spatial zoom may be uncomfortable or visually unstable on small screens. Preserve identity without preserving every pixel of travel.

## Orientation and resizing

Recompute scroll distances and layout-dependent animation after meaningful resizes. Do not let old pixel measurements survive a breakpoint change.

When possible, use library-supported media-query lifecycle such as `gsap.matchMedia()` [R12] rather than manually accumulating duplicate animations.

## Touch

Touch users need:

- adequate targets;
- predictable native scrolling;
- no hover-only dependency;
- no accidental horizontal capture while trying to scroll vertically;
- drag affordances only where dragging is useful and discoverable.

## Reduced motion is separate from mobile

Do not assume mobile users want less motion or desktop users want more. Responsive behavior and motion-preference behavior are independent dimensions.
