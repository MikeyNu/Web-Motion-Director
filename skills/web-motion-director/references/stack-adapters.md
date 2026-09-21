# Stack adapters

## Selection principle

Choose the smallest dependable system that expresses the motion. Existing project conventions win unless there is a concrete defect or missing capability.

## CSS transitions and keyframes

Best for:

- hover and focus;
- button press;
- simple menu icon changes;
- opacity, transform, color, and clip changes;
- straightforward loading indicators;
- small repeated interactions.

Prefer CSS when JavaScript does not need to coordinate state or cancel complex timelines.

Avoid `transition: all`; list the properties that should animate.

## Web Animations API

Best for:

- vanilla JavaScript projects;
- animations that need imperative play, pause, reverse, cancel, or timing control;
- component logic without a third-party dependency.

Keep animation objects scoped and cancel them on teardown.

## View Transition API

Best for:

- continuity between DOM states;
- same-document transitions;
- supported same-origin cross-document navigation;
- shared named elements and route-level transitions.

Always preserve normal navigation fallback and check target browser support at implementation time.

## CSS scroll-driven animations

Best for:

- simple progress-based effects;
- effects that can be expressed declaratively;
- projects whose browser support matrix allows the relevant features.

Do not choose this solely to avoid JavaScript when the choreography actually needs measurement, pinning, nested state, or advanced lifecycle management.

## Motion for React

Best for:

- enter/exit presence;
- React layout transitions;
- drag and gesture interactions;
- spring behavior;
- component-scoped animation;
- relatively simple scroll mappings.

Prefer the project’s existing Motion patterns if already installed. Do not add GSAP just to replace Motion for effects Motion already handles well.

## GSAP

Best for:

- complex timeline coordination;
- precise sequence control;
- scrubbed scroll scenes;
- pinning;
- horizontal transformed chapters;
- SVG/path animation;
- advanced layout transitions with Flip;
- imperative creative-development workflows.

### React lifecycle

Use a scoped lifecycle helper or context and clean up on unmount. For breakpoint-specific scenes, `gsap.matchMedia()` can create and revert ScrollTriggers and animations as media queries change. [R12]

### ScrollTrigger

Measure real elements. Refresh after layout-affecting media and fonts where needed. Avoid creating a new trigger on every render.

## Lenis or smooth-scroll engines

Use only when the brand experience genuinely benefits from modified scroll feel and the existing accessibility and navigation behavior can be preserved.

If used with GSAP:

- synchronize the scroll source and animation ticker correctly;
- avoid a second competing smooth-scroll library;
- test anchor links, keyboard scrolling, focus, reduced motion, mobile, browser back/forward, and fixed/sticky elements.

## Three.js / React Three Fiber

Best for:

- true 3D objects;
- camera journeys;
- shader-driven environments;
- spatial narratives;
- product visualization where the scene itself carries value.

Not appropriate merely to animate a card or background gradient.

Performance rules:

- lazy-load the scene;
- keep critical HTML outside the canvas;
- cap rendering cost on constrained devices;
- pause or reduce work off-screen;
- provide a static or simplified fallback;
- do not hide navigation inside WebGL alone.

## Lottie or Rive

Use when the project has suitable animation assets or state machines and the runtime cost is justified. Do not convert every UI transition into an exported animation file, because live HTML controls and state should remain semantic.

## No library

A static interface can be the correct output. A skill that always installs animation dependencies is failing its design role.
