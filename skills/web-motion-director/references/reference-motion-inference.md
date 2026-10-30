# Motion evidence from static and temporal references

## Core rule

A screenshot proves a resting composition. It does not prove how the original page animated.

When reconstructing from a still image, preserve required visual fidelity and treat motion as a proposal unless video, prototype data, Figma motion, source code, or another temporal reference is available. Consider appearance and motion together; checking the resting state does not require postponing all temporal design until the layout is finished.

## What can be observed

Record evidence such as:

- objects crossing section boundaries;
- overlapping layers;
- crop direction and gaze;
- off-screen continuation of a row or media strip;
- repeated cards or panels;
- masks and clipping shapes;
- apparent depth layers;
- persistent-looking navigation;
- large typography that could change role while scrolling;
- a visual object repeated between list and detail states;
- section geometry that suggests a sticky frame.

## What can only be inferred

Do not present these as known from one screenshot:

- exact animation trigger;
- easing curve;
- duration;
- pinning behavior;
- scroll velocity relationship;
- route transition;
- hover behavior;
- menu choreography;
- autoplay behavior;
- animation order before or after the captured state.

## Motion reconstruction hierarchy

1. Use actual motion evidence if supplied.
2. Inspect existing source if the reference comes from a current codebase.
3. Reuse known design-system motion patterns if the product already has them.
4. Propose a coherent motion direction from the visual relationships and desired experience, including beauty or enjoyment. Do not automatically equate smallest with best.
5. Prototype the principal sequence and compare its actual effect. Keep quiet regions where they strengthen the whole; avoid applying the same animation to every region.

## Plausible mappings

### Visual bridge across sections

If one object visually crosses a section boundary, it may serve as a transition object while the background or copy changes. Keep the object stable enough that it creates continuity rather than random parallax.

### Media rail

If multiple media items visibly extend beyond the viewport, test whether a native rail, drag interaction, or bounded vertical-to-horizontal chapter fits the content. Do not assume it must be horizontally animated.

### Layered hero

If a hero contains distinct foreground and background layers, subtle differential movement may add depth. Avoid strong parallax in high-trust or text-heavy contexts, and remove spatial movement in reduced-motion mode.

### Repeated list-to-detail media

If the same image or object is clearly present on a listing and detail route, shared-element continuity is a strong candidate.

### Pinned-looking title

A section title that visually anchors a cluster of content can remain sticky while its associated items progress. Verify that the title does not obscure focus or reading on smaller screens.

## Verification against reference

For temporal sources, inspect normal-speed playback and timestamped onset, intermediate, and settled states. Record supported inputs and uncertainty. Distinguish product animation from camera movement, editing cuts, and speed changes. Sampled frames alone do not establish smoothness or exact easing. Use the [joint reference protocol](graphic-design-coordination.md#reference-evidence); do not invent measurements or implementation technology from appearance.

Motion enhancement must not damage static parity. At the reference viewport:

- inspect the resting state against the supplied image;
- sample the start and end of the proposed movement;
- confirm that the final resting composition still matches the reference where required;
- ensure clipping, masks, and z-index behavior remain correct;
- verify that responsive changes do not expose hidden reference artifacts.

## Temporal reconstruction worksheet

For each principal sequence, record source identity and nominal media metadata, approximate source timestamps, visual layers, stable anchors, order/overlap/hold, supported input, uncertainties, and a proposed implementation. Classify movement inside footage separately from movement of its container. A rotating tablet, tilted page sheet, or showcase zoom is not automatically part of the product.

Record first readability, visible controls, and visual settlement separately; a visible control does not establish input readiness unless an interaction demonstrates it. Exact frame timestamps locate samples; they do not locate the original onset more precisely than the sampling interval. Increase sampling around clipping, crossing, or reversal; inspect source-resolution crops when details matter. Do not infer smoothness from contact sheets or production performance from recording frame rate.

See the [owner's nine-clip study](https://github.com/MikeyNu/agent-graphic-designer/blob/main/skills/graphic-design/references/owner-motion-study.md) for a completed example with explicit limits. Use [Motion principles and choreography](motion-principles-and-choreography.md) to turn observations into an independent construction. Preserve a source's actual behavior only when faithful reconstruction is requested; inspired adaptation can change the mechanism.

## Reporting language

Use wording such as:

- “The screenshot supports this composition; the transition is an inferred motion direction.”
- “No temporal reference was supplied, so timing and easing are design proposals.”
- “The original animation cannot be recovered from the still image alone.”

Do not use “exact animation recreation” without actual motion evidence.
