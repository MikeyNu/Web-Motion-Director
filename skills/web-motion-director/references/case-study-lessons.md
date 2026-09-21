# Case study lessons

These examples are used to reason about principles. Do not copy their recognizable identities.

## Dondre Green portfolio

Source: [R16]

Useful lessons:

- hero typography can change role during scroll instead of simply disappearing;
- images can become focused based on viewport position;
- a section title can remain pinned while related media progresses;
- page transitions can use a brand-relevant metaphor such as a shutter.

Transferable principle: build motion from the content medium and brand, not from a universal reveal preset.

## Podium

Source: [R14]

Useful lessons:

- the selected media becomes the route-transition object;
- a more decorative pixel transition was removed because it distracted from the content;
- GSAP Flip, Lenis, and Three.js were used where each had a distinct responsibility.

Transferable principle: the strongest transition may be the content itself. Remove effects that compete with the focal object.

## The Spark

Source: [R17]

Useful lessons:

- storyboard narrative beats before deciding tools;
- allocate different scroll ranges according to pacing;
- activate heavy scenes selectively;
- coordinate DOM and graphical layers from one scroll model.

Transferable principle: immersive motion is an authored runtime system, not a long page with random 3D sections.

## Maxima Therapy

Source: [R19]

Useful lessons:

- healthcare-related experiences can support playful motion when the organization’s identity is warm and illustrative;
- controls can morph and stickers can react directly to input;
- scroll-linked effects can coexist with interaction-level motion.

Transferable principle: domain seriousness does not automatically mean zero motion. Brand, audience, task, and trust determine posture.

## Infinite GSAP gallery with Flip

Source: [R20]

Useful lessons:

- the transition can preserve visual identity even when source and destination use different DOM elements;
- parallax, reveal, and route transition are separate systems with separate jobs;
- transition identity needs explicit coordination.

Transferable principle: shared-element continuity can bridge large layout changes without a generic overlay.

## The Never Ending Story

Source: [R15]

Useful lessons:

- a minimal site can become memorable through one coherent interaction model;
- infinite scrolling, parallax, and snapping were combined around a gallery concept;
- the authors frame motion as a way to make less feel like more, not as a pile of effects.

Transferable principle: a small number of strong rules can outperform many disconnected animations.

## Scroll-driven 3D portfolio

Source: [R18]

Useful lessons:

- 3D is justified when the intended experience is environmental and spatial;
- tools such as Three.js, shaders, GSAP, and Blender serve that concept.

Transferable principle: use 3D when space is part of the message, not because the site needs “more animation.”

## Interactive comic

Source: [R22]

Useful lessons:

- scroll velocity can influence secondary atmosphere;
- chapters can assemble into place rather than simply fade in;
- WebGL and DOM text can remain separate layers coordinated by one progression model.

Transferable principle: dynamic background behavior is most defensible when it reinforces a narrative concept and remains secondary to content.

## Summary heuristics

Across the case studies:

1. Motion begins with a concept or content relationship.
2. One strong continuity object often works better than a generic page wipe.
3. Scroll chapters need explicit pacing and boundaries.
4. Heavy graphical scenes require lifecycle and performance planning.
5. Teams often remove effects that distract, even when those effects are technically impressive.
6. Motion systems are composed from multiple layers with clear ownership, not one library blindly used for every problem.
