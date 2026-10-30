# Motion strategy

## Purpose

Use this guide before writing animation code. The central task is to convert product intent into a coherent motion system.

## Motion roles

Every substantial animation should primarily serve one or more roles:

- **Feedback:** confirm input, success, error, loading, or selection.
- **Continuity:** preserve a user’s mental model across state or route changes.
- **Hierarchy:** direct attention toward the next important object or action.
- **Spatial explanation:** show where something came from, where it moved, or what contains it.
- **Narrative:** establish sequence, reveal causal relationships, or control pacing.
- **Demonstration:** show how a product, process, or interaction behaves.
- **Brand character:** make motion feel specific to the identity when it does not compete with the task.
- **Aesthetic experience:** create beauty, rhythm, atmosphere, surprise, or play. A measured functional benefit is not required.

Explore the actual sequence before deciding that restraint or expression is stronger. Avoid automatic animation recipes, but do not require a functional metaphor for ornament. Read [Graphic-design coordination](graphic-design-coordination.md) and plan movement while composing the interface.

## Surface posture

### High-trust healthcare, finance, civic, enterprise

Favor fast state transitions, subtle spatial continuity, clear dialog and drawer motion, reliable route changes, restrained image movement, and strong reduced-motion behavior. Richer narrative motion can exist on marketing pages when it supports the brand, but operational tasks should remain predictable.

### Commerce

Use motion to aid product inspection, gallery selection, cart feedback, filters, comparison, and continuity from product listing to detail. Do not put spectacle between a shopper and product information.

### Editorial

Let typography and media lead. Motion may support chapter changes, image focus, annotations, timelines, or controlled horizontal media sequences. Avoid breaking ordinary reading.

### Portfolio and entertainment

More expressive motion can be appropriate because experience quality is part of the value. Even here, navigation and escape routes must remain reliable.

### Education

Motion can reinforce cause and effect, progression, feedback, and play. Do not use movement that competes with reading or learning goals.

## Motion thesis template

```text
Character:
Primary role of motion:
Dominant axis or spatial logic:
Stable anchors:
High-motion zones:
Quiet zones:
Tempo:
Easing family:
Navigation model:
Scroll model:
Mobile transformation:
Reduced-motion model:
Performance constraints:
```

## Divergent exploration

For major work, compare at least three strategies. A useful set is:

1. **Continuity-first:** minimal animation, shared elements, spatial drawers, route continuity.
2. **Editorial choreography:** controlled sticky sections, media focus, text and image sequencing.
3. **Immersive:** deeper scene transitions, WebGL or 3D, sound or camera motion if justified.

This list is illustrative, not a required restrained/editorial/3D ladder. Compare genuinely plausible approaches for the same task; alternatives may all use CSS and differ in object relationships, staging, or sequence. Share visible roughs with the graphic-design workflow. Preserve the approved direction during a narrow repair or scoped feature extension.

Evaluate aesthetic quality, rhythm, character, task clarity, information hierarchy, accessibility, responsive behavior, implementation feasibility, performance, and maintenance. A visually compelling experience is a valid goal. Let a principal motion prototype inform the layout before either is considered complete.

## Tempo and hierarchy

A motion system needs different strengths.

- **Micro:** approximately 80 to 250 ms for repeated feedback and small control changes.
- **Component:** approximately 180 to 450 ms for menus, drawers, cards, filters, and layout changes.
- **Page or narrative:** approximately 300 to 900 ms for deliberate route continuity or scene changes, with longer scroll-linked sequences controlled by user progress instead of fixed time.

These are starting ranges, not rules. Repeated operational interactions should be faster than cinematic brand sequences.

## Easing posture

- Use ease-out for elements entering or reacting to user actions.
- Use ease-in for elements intentionally leaving when the exit deserves perception.
- Use ease-in-out for controlled continuous changes.
- Use linear progress for scroll-scrubbed mapping unless the experience intentionally remaps progress.
- Choose springs for appropriate spatial response and retargeting; tune damping and overshoot separately. A spring does not require visible bounce. Elastic rebound is an expressive choice, not a universal default.
- Do not use identical easing for every interaction by habit.

These are candidate postures, not hard mappings. A panel that remains conceptually nearby can settle offscreen instead of accelerating away. Choose a curve, spring, or progress model by its actual response. Read [Motion principles and choreography](motion-principles-and-choreography.md) for the four clocks, sequence scoring, construction, and evidence. Initial feedback, input readiness, and decorative completion need not share one deadline.

## Stable anchors

Strong motion often works because something stays still. Examples include:

- a pinned section title while related media advances;
- navigation remaining stable while content transitions;
- a selected image remaining visually continuous between listing and detail;
- a stable product frame while specifications change;
- a fixed narrative environment while foreground chapters progress.

Identify the stable anchor before designing movement.

## Motion budget

For each route, decide how many areas can carry high-attention motion simultaneously. One strong motion chapter can be more memorable than ten generic reveals.

Use quiet sections to let users read, recover, and understand location.
