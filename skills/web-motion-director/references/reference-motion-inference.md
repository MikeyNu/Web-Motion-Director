# Motion inference from static references

## Core rule

A screenshot proves a resting composition. It does not prove how the original page animated.

When reconstructing from a still image, preserve visual fidelity first and treat motion as a proposed enhancement unless video, prototype data, Figma motion, source code, or another temporal reference is available.

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
4. Infer the smallest product-specific motion that improves the static composition.
5. Keep the page static if motion would be arbitrary.

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

Motion enhancement must not damage static parity. At the reference viewport:

- inspect the resting state against the supplied image;
- sample the start and end of the proposed movement;
- confirm that the final resting composition still matches the reference where required;
- ensure clipping, masks, and z-index behavior remain correct;
- verify that responsive changes do not expose hidden reference artifacts.

## Reporting language

Use wording such as:

- “The screenshot supports this composition; the transition is an inferred motion direction.”
- “No temporal reference was supplied, so timing and easing are design proposals.”
- “The original animation cannot be recovered from the still image alone.”

Do not use “exact animation recreation” without actual motion evidence.
