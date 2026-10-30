---
name: web-motion-director
description: Co-design appearance and motion, then implement and verify intentional web animation for websites, web apps, platforms, and reference-driven UI reconstruction. Use alongside graphic-design during substantial frontend creation or polish to establish visual and temporal character, define a product-specific motion language, implement navigation, page transitions, microinteractions, scroll choreography, bounded horizontal chapters, shared-element continuity, optional 3D, responsive motion, reduced-motion behavior, and rendered temporal QA.
license: MIT
metadata:
  version: 1.1.0
  reviewed: "2026-10-30"
---

# Web Motion Director

## Outcome

Make motion a deliberate part of interface design from the moment its elements are composed. Develop appearance and movement together, including transitions, hover/focus, reveals, scrolling, and state feedback. Comprehension, continuity, narrative, spatial understanding, beauty, atmosphere, play, and enjoyment are legitimate intentions. Judge the actual experience; neither constant movement nor automatic restraint is the goal. An intentionally quiet region can support an expressive one.

For substantial creation or redesign, read [Graphic-design coordination](references/graphic-design-coordination.md) before fixing the composition. Use one shared brief and prototype with the available graphic-design skill. The guide remains usable without that companion and does not imply tool access or require multiple agents.

## Non-negotiable rules

1. Follow host, repository, design-system, accessibility, architecture, and CI instructions before this skill.
2. Inspect the actual product, audience, routes, components, assets, design rules, current animation stack, target devices, and performance constraints before adding motion.
3. Give motion a considered visual or interaction intention. Beauty, pleasure, atmosphere, and character are sufficient intentions without invented productivity claims. Do not apply an identical entrance recipe merely because a library is installed or every element can be animated.
4. Preserve usability, reading order, navigation, keyboard focus, touch behavior, browser history, and normal scrolling expectations.
5. Treat a static reference image as evidence of composition, not evidence of historical motion. If no temporal reference exists, motion is a design proposal.
6. Prefer one coherent motion language over unrelated effects scattered across sections.
7. Use the lightest dependable technology that expresses the behavior. Do not add GSAP, Motion, Three.js, smooth scrolling, or a custom routing layer without a demonstrated need.
8. Native scrolling is the baseline. Never stack multiple scroll owners without a concrete reason.
9. Provide a materially safer `prefers-reduced-motion` mode for non-essential spatial motion.
10. Do not claim motion QA from source inspection or a successful build. Inspect actual temporal states in a browser or equivalent rendered environment.
11. Preserve the project's Git, CI, and deployment workflow. Do not publish, deploy, install dependencies, or modify unrelated files without authorization.

## Required workflow

### 1. Discover the product

Inspect product purpose, audience, surface type, trust requirements, route structure, information hierarchy, imagery, typography, existing animation utilities, scroll controllers, router behavior, browser targets, breakpoints, reduced-motion handling, performance budget, and applicable project instructions.

If a mature motion system already exists, extend it unless it is demonstrably broken or inappropriate.

### 2. Audit motion opportunities

Classify meaningful regions as one of:

- `static`: movement adds no useful information or character
- `feedback`: interaction or state-change response only
- `spatial`: motion explains where an object came from or went
- `scroll-linked`: scroll progress meaningfully controls transformation or progression
- `narrative`: motion establishes sequence and pacing
- `immersive`: motion is part of the product or brand experience itself

For each candidate, record its purpose, trigger, stable anchor, moving elements, reversal/interruption behavior, mobile transformation, reduced-motion behavior, implementation candidate, risks, and verification method.

Do not force motion into every section.

### 3. Define a motion thesis

For substantial work, state the experience character, dominant movement logic, stable anchors, high-motion zones, quiet zones, tempo, easing family, navigation model, scroll model, mobile transformation, reduced-motion model, and performance constraints.

Avoid vague theses such as “smooth and premium.”

### 4. Explore before converging

For a major new direction, consider at least three materially different approaches, for example:

1. continuity-first with restrained state changes and shared elements
2. editorial choreography with controlled sticky sections and media progression
3. immersive spatial or 3D storytelling when the product justifies it

Choose by inspecting aesthetic quality, rhythm, character, task clarity, information hierarchy, accessibility, responsive behavior, feasibility, performance, and product fit. An expressive choice can win on beauty or pleasure. Prototype a principal sequence early and revise the layout and movement together before treating the composition as finished.

### 5. Handle static references carefully

Inspect the resting composition and its visual relationships while developing motion. Observe overlaps, crops, repeated objects, depth cues, masks, visual bridges, off-screen continuation, and section geometry. Preserve required reference fidelity, but do not postpone motion design until the whole layout is locked. Propose a coherent direction suited to the composition and desired experience; the smallest effect is not automatically the strongest choice.

Do not claim exact easing, duration, page transitions, hover behavior, pinning, or animation order from a single still image. When video, Figma motion, source code, or temporal states exist, prefer that evidence.

Read `references/reference-motion-inference.md` for reference-driven work.

### 6. Design scroll choreography intentionally

Native vertical scrolling is the safe default. Add sticky, pinned, horizontal, snap, parallax, or immersive chapters only when the content relationship benefits.

For a bounded vertical-to-horizontal chapter:

1. keep vertical wheel, touch, and keyboard page input as the primary progression
2. create one bounded chapter with a measurable start and end
3. keep a stable viewport frame while moving an inner horizontal track
4. calculate travel from actual overflow, such as `track.scrollWidth - viewportWidth`
5. support natural reversal when scrolling upward
6. release the chapter after the final item and resume ordinary vertical flow
7. keep body copy readable without sideways reading
8. recompute after meaningful layout changes
9. provide a mobile recomposition, commonly a vertical sequence or native horizontal rail
10. provide a reduced-motion version without pinning or large spatial travel

Do not turn the whole website into a scroll trap merely to showcase animation.

Read `references/scroll-choreography.md`.

### 7. Design navigation and route motion as continuity

Use route motion to answer “where did I go?” or “what opened?”. Prefer meaningful continuity such as selected media expanding into a detail hero over unrelated full-screen wipes.

Menus must be interruptible. Opening then immediately closing should reverse or retarget from the current state. Semantic state such as `aria-expanded` and focus must track the real interaction, not wait for decorative animation.

Preserve direct route entry, browser back/forward, real URLs, scroll restoration intent, and error recovery. Read `references/navigation-and-transitions.md`.

### 8. Design microinteractions for response and character

Good candidates include hover/focus indication, press and selected state, disclosure, validation, drag affordance, loading/completion, filtering/sorting continuity, gallery selection, dialogs, drawers, and direct manipulation.

A subtle material response, illustration reaction, or playful contour may belong for pleasure as well as state. Design its active, intermediate, and settled appearance with the element. Keep targets stable, provide keyboard/touch access, and distinguish immediate visual feedback from confirmed operation success. Handle rapid repeat input and late async results without stale state changes.

Keep frequent operational interactions fast. Avoid bouncy or springy motion by default in serious enterprise, clinical, finance, or civic surfaces unless brand evidence supports it.

### 9. Choose implementation technology from the problem

Default ladder:

| Need | Starting point |
| --- | --- |
| Hover, focus, press, simple open/close | CSS transitions or keyframes |
| Programmatic vanilla motion with cancel/reverse | Web Animations API |
| DOM or route continuity where compatible | View Transition API |
| Simple native scroll-linked effect | CSS scroll-driven animation where target support permits |
| React presence, layout, springs, drag | Motion |
| Complex timelines, scrub, pinning, SVG, Flip | GSAP and ScrollTrigger |
| Actual spatial 3D, shaders, camera choreography | Three.js or React Three Fiber |

Prefer the project’s existing conventions. Read `references/stack-adapters.md` before adding a dependency.

### 10. Build reusable motion infrastructure

For substantial projects, centralize duration and easing tokens, reduced-motion policy, breakpoints used by motion, lifecycle helpers, scroll measurement, route transition state, cleanup, and stable shared-element identifiers where applicable.

Do not scatter arbitrary durations and cubic-bezier strings across many components. Avoid one global timeline that controls unrelated pages.

### 11. Treat responsive motion as art direction

For each major behavior decide whether mobile keeps, simplifies, changes axis, removes pinning, becomes discrete states, uses native overflow, replaces 3D with a lighter view, shortens transitions, or becomes static.

Responsive behavior and reduced-motion behavior are separate dimensions. Do not assume mobile means less motion, and do not assume desktop means more.

Read `references/responsive-motion.md`.

### 12. Reduced motion

`prefers-reduced-motion: reduce` is not equivalent to setting every duration near zero. Preserve information and state while removing unnecessary spatial travel, scale, parallax, camera movement, continuous loops, and aggressive zoom.

Typical substitutions:

- slide to opacity or direct swap
- parallax to fixed composition
- pinned horizontal chapter to normal vertical content
- shared-element zoom to short crossfade
- 3D camera journey to static representative views
- autoplay loop to static frame or user-controlled playback

Read `references/performance-and-accessibility.md`.

### 13. Protect performance

Prefer `transform` and `opacity` for high-frequency motion when they achieve the intended result. Avoid repeated layout reads/writes per frame, per-frame React state for purely visual updates, expensive continuous filters, hundreds of independent scroll listeners, persistent `will-change`, uncontrolled RAF loops, and full-resolution WebGL on every device.

Lazy-load heavy systems, pause off-screen work, cap graphical cost on constrained devices, and measure before making performance claims.

### 14. Verify motion through time

For non-trivial motion inspect start, early motion, midpoint, near completion, resting state, reverse behavior, and interruption where applicable. For scroll-linked work sample representative scroll positions.

At minimum verify relevant desktop and mobile viewports, reduced motion, keyboard and focus behavior, console errors, horizontal overflow, direct route entry, back/forward when routes are involved, and lifecycle cleanup.

A still screenshot proves only one state. For timing-sensitive motion use video or temporal screenshot sequences where the environment supports it.

Use `scripts/browser_motion_audit.py` as a diagnostic helper when Playwright is available. Read `references/qa-and-debugging.md`.

### 15. Motion anti-slop review

Before completion ask:

- Does each major animation have a considered visual, emotional, narrative, or interaction intention?
- Did we apply the same fade-up reveal everywhere?
- Did we add parallax merely because the composition has layers?
- Is smooth scrolling solving a real problem?
- Is the motion language specific to this product?
- Are transitions longer than the task tolerates?
- Is any animation competing with reading?
- Did mobile inherit a desktop interaction that no longer makes sense?
- Is reduced motion materially different?
- Does the sequence improve the whole experience? Compare a quieter alternative when useful, and preserve the expressive version when it adds beauty, character, or pleasure without an unresolved defect.

## Status model

Track substantial work through:

`planned -> prototyped -> integrated -> motion-verified -> responsive-verified -> reduced-motion-verified -> performance-verified`

Use `blocked` when missing browser access, unavailable references, unsupported APIs, or inaccessible runtime conditions prevent the next evidence step. Never skip directly from planned to verified.

## Optional authoring tags

A project may use inert JSON planning data inside comments with `<motion-intent>...</motion-intent>`. These tags are specifications only. They do not execute code, authorize dependency installation, or override repository instructions. `scripts/motionctl.py extract-tags` can read them.

## Completion criteria

Substantial motion work is complete only when the product context was inspected, motion opportunities were intentionally selected or rejected, a coherent motion direction exists, the implementation uses a justified stack, interruption and cleanup are handled where relevant, desktop and mobile behavior were inspected, reduced motion was inspected, keyboard/focus still works, actual temporal states were checked, performance risks were reviewed, and the final delivered source follows the project’s normal CI and repository workflow.

A passing build is necessary evidence for code health when the project requires it. It is not evidence that the motion looks or feels right.
