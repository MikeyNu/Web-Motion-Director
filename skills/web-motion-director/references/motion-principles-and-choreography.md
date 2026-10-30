# Motion principles and choreography

Use when designing a signature sequence, translating a temporal reference, or making existing motion feel deliberately composed. This guide combines official platform guidance, scoped research, and original synthesis from the owner's nine clips. Read the [research register](../RESEARCH.md#30-october-2026-motion-principles-research) for evidence and limits, and the [timestamped clip study](https://github.com/MikeyNu/agent-graphic-designer/blob/main/skills/graphic-design/references/owner-motion-study.md) for observations. Neither proves the original implementation or the quality of a future prototype.

## Contents

- [1. Design relationships before effects](#1-design-relationships-before-effects)
- [2. Separate the clocks](#2-separate-the-clocks)
- [3. Score a sequence](#3-score-a-sequence)
- [4. Choose a motion model](#4-choose-a-motion-model)
- [5. Construct the visual mechanisms](#5-construct-the-visual-mechanisms)
- [6. Preserve control and state truth](#6-preserve-control-and-state-truth)
- [7. Adapt without losing the idea](#7-adapt-without-losing-the-idea)
- [8. Judge the result through time](#8-judge-the-result-through-time)

## 1. Design relationships before effects

Ask what makes the sequence compelling: an image surviving a change of context, a shape revealing a new world, a pleasing response to touch, a typographic collision, or the rhythm of a group assembling. Name the visual relationship before selecting an animation library. Beauty, atmosphere, humor, and delight are valid intentions. A functional explanation is not required for every flourish.

Classical animation craft can inform interfaces without making every control act like a cartoon character. The following are design heuristics, not experimentally proven prescriptions for all UI:

| Principle | Apply to an interface | Watch for |
| --- | --- | --- |
| Staging | Establish a focal object, readable field, and supporting activity. Decide what leads attention. | Several equally loud motions, or a sequence that hides the next action. |
| Continuity | Retain object identity, crop, origin, or spatial relationship across change. | An unrelated photograph pretending to be the same object; a route with no direct-load state. |
| Anticipation | Use a press response, a slight preview, or a meaningful indication of direction. | A theatrical wind-up that delays the requested action. |
| Follow-through and overlap | Let supporting strokes or details finish after the main object arrives; start related arrivals before predecessors fully stop. | Every child waiting in a long queue, or decorative finish delaying focus and input. |
| Timing and spacing | Tune both the total interval and how far an object travels between moments. | Changing only duration while leaving abrupt velocity, long dead time, or excessive travel. |
| Weight and material | Make a rigid plane, soft illustration, line drawing, and photograph respond differently where that improves the idea. | Stretching text or media accidentally; assuming spring physics must visibly bounce. |
| Arcs and direction | Follow a coherent path when it reinforces spatial attachment or play. Straight travel can suit architectural geometry. | Curved detours on routine navigation or directional meaning that changes unpredictably. |
| Exaggeration and contrast | Amplify one chosen gesture and give it quieter neighbors. | Scaling every element, losing the target, or erasing a deliberate expressive identity through automatic restraint. |
| Rhythm and holds | Compose arrival, overlap, pause, and departure as a phrase. | A hold that traps the user, perpetual movement, or identical punctuation at every section. |
| Appeal | Judge silhouette, crop, proportion, contour, and rhythm together at real size. | Claiming that correct terminology, a popular easing curve, or checklist compliance proves beauty. |

In data graphics, Heer and Robertson's experiments support animation and some simple staging for the examined tracking and change-estimation tasks, while complex staging sometimes increased error. This is a reason to inspect occlusion and unnecessary phases, not proof that every UI needs staged entrances or a fixed duration. See R27.

Platform systems offer useful but situated choices. Carbon distinguishes productive and expressive motion and separates component responses from page choreography. Material's motion system distinguishes spatial movement from visual effects. Apple emphasizes responsiveness and motion that can be interrupted. Adopt relevant relationships, not their complete brand vocabulary as universal law. See R23 through R26.

## 2. Separate the clocks

| Clock | What it establishes | Do not confuse it with |
| --- | --- | --- |
| Recording time | Where an observed frame occurs in a supplied clip. | The original animation duration, real interaction latency, or an unedited capture. |
| Elapsed animation time | A time-based transition after an event or threshold. | A requirement to block the task until decorative settlement. |
| User progress | Gesture position, scroll geometry, or explicit step selection. | Autoplay time; a scrubbed scene cannot be specified by milliseconds alone. |
| Application/data state | Selection, route, pending request, confirmed result, failure, cancellation. | A timer or animation completion callback that can fabricate success. |

State which clock owns each sequence. A scroll threshold can launch an elapsed-time reveal; that is different from scroll continuously controlling the reveal. Async data can arrive while either is running. Define the handoff instead of allowing competing clocks to overwrite each other.

For scroll-linked choreography, establish a shared progress value from actual start/end geometry. Derive each visual beat from a bounded subrange. As planning notation, `local = clamp((progress - start) / (end - start), 0, 1)` describes a subrange when `end > start`. Keep direct tracking linear by default; easing a decorative subrange is a deliberate remapping to inspect in both directions. An independent tween that restarts on every scroll event is not faithful progress tracking.

## 3. Score a sequence

Use a short beat table for the principal scene. Record origin, travel, crop, mask, layer order, opacity, and the stable anchor. Separate **first useful/readable state**, **input readiness**, and **visual settlement**. These often occur at different times. Input can become available before accents settle, provided targets and feedback are already dependable.

Example design proposal for a new illustrated collection opening, not measured from a reference:

| Relative phase | Visual beat | State and control |
| --- | --- | --- |
| Trigger | Selection responds; existing context remains visible. | Record the selected item immediately; honor another selection. |
| Early | The selected image begins changing frame; the destination surface establishes itself. | Navigation may proceed; preserve direct entry and failure recovery. |
| Overlap | Heading becomes readable while the frame is still settling. | Expose the meaningful destination state; focus follows the actual navigation contract. |
| Follow-through | A small original line or texture detail finishes. | Do not delay input, success, or accessibility announcements for ornament. |
| Hold | The complete composition rests. | No compulsory dwell; users may continue, reverse, or leave. |

Choose actual timings or progress intervals after considering distance, object size, frequency, content, input, and the established system. Record trial values honestly, then tune at normal speed. For a time-based stagger of equal-duration items, total completion is approximately `duration + (count - 1) * offset`, not just the duration of one item. A pleasant four-card entrance can become an intolerable forty-row queue. Limit, group, or remove stagger as content grows.

Design overlap intentionally. Related objects may share onset, follow by a small phase offset, or move concurrently with different envelopes. Simultaneity can express a group; staggering can establish order. Neither always improves comprehension. Use holds to let an image or phrase register, with user control intact.

Do not force a new introduction on every viewport re-entry or data refresh. Define first entry, deliberate replay, state update, and return behavior separately. Frequent actions must still feel good after repeated use.

## 4. Choose a motion model

| Model | Useful when | Specify and inspect |
| --- | --- | --- |
| Duration and easing | A defined reveal, short state transition, or intentionally timed graphic phrase. | Duration, curve, delay, overlap, and interruption from the current appearance. |
| Spring | Retargetable spatial response, direct manipulation, or a material settling gesture. | The implementation's stiffness/damping model, starting velocity, overshoot, settlement, and rapid retargeting. |
| Progress mapping | Scroll or gesture position should own the scene. | Geometry, subranges, reverse traversal, bounds, release, and resize. |
| Media timeline | Footage, rendered image sequences, or audio-synchronized content is the actual artwork. | Loading, decoding, seek behavior, playback control, fallback, and rights. |

A spring need not be bouncy. Well-damped spring movement can be suitable in serious products; uncontrolled overshoot is a separate decision. Do not ban spring technology by sector or apply elastic rebound to every component. Material's spatial/effects distinction is useful here: movement may overshoot deliberately while opacity, color, and other bounded values should settle without invalid excursions. Inspect the actual implementation's behavior rather than assuming every spring API preserves velocity or cancels work identically.

Ease-out is a useful candidate for prompt arrival, ease-in for some departures, and ease-in-out for some visible-to-visible changes. These are starting choices. A drawer that remains conceptually nearby may settle at its edge rather than accelerating away like a discarded object. Infinite linear rotation and direct scroll tracking are also legitimate; “linear is always unnatural” is not a portable rule.

Use the project's established motion tokens when suitable. Tokenize recurring semantic responses, not arbitrary effects such as `coolBounce`. Add only the distinctions the product actually needs. A brand scene can have its own score without a global timeline controlling unrelated routes.

## 5. Construct the visual mechanisms

The following are plausible implementation approaches inspired by C01 through C09, not recovered source code. Choose with the actual stack and target support; no listed library is required.

### Mask and aperture reveals

Keep the image's proportions independent of the changing window. Reveal a full-size image with clipping, a mask, or an overflow wrapper instead of applying `scaleY` to its pixels. Decide whether the image remains fixed, counter-moves, or gently reframes inside the window. The aperture's contour and origin should belong to the art direction. C02 repeats a recognizable shape; C04 uses slits that grow into varied image windows.

For C09-like shutters, align every slice to one shared full-image crop and focal point. Separate narrow `cover` images will usually disagree at the seams. Inspect partial reveals at actual device pixel ratio, fractional widths, resizing, and contrasting backgrounds. Keep a stable container and avoid hairline gaps or doubled edges. Complex masks may incur paint cost; profile the rendered version.

### Typography, clipped labels, and image intersections

Animate a visual wrapper while keeping semantic text whole. Line reveals should respect real wrapping, ascenders, descenders, accents, and font loading. Character splitting can damage shaping, selection, and accessibility, particularly in connected scripts; prefer line/word/group treatment where it fits, or avoid splitting. Recalculate only when necessary and restore the readable baseline if enhancement fails.

C01's CTA suggests a moving fill and rolling visual label. Keep a stable button hit area and one accessible name; visual copies must not create duplicated speech or duplicate tab stops. C05's contrasting letter segments can be explored with aligned clipped duplicates; blend modes are an alternative with different color/contrast risks. Check intermediate collisions, not only the polished endpoint.

### Shared-object expansion

Preserve the selected image or object while its frame changes role. Maintain subject/focal-point continuity, appropriate crop, border radius, and layer order. Measure the source and destination at the relevant lifecycle point; do not assume the destination asset or layout is already available. Provide direct navigation if geometry or media is missing. A transformed visual layer must not create a second semantic control or steal focus.

Handle a new selection, Back, route failure, and resize during the transition. Remove obsolete overlays. On return, restore meaningful selection and scroll context, even if the spatial animation is skipped. C09's recognizable purple landscape illustrates the relationship; the footage does not establish its routing technology.

### Linked progress, rings, and counters

Drive related visuals from one state or progress source. A ring, week marker, card emphasis, and track position can describe a single chapter without independent timers drifting apart. Keep discrete content changes deliberate and synchronize label, value, unit, and scope.

Separate decorative digit rolling from real data. Do not tween between unrelated metrics, fabricate progress, or imply a saved value before confirmation. Avoid announcing every intermediate digit to assistive technology. A final static label must remain available. Preserve data truth when animation is skipped, reversed, interrupted, or never loaded.

### Drawn accents and bounded kinetic illustrations

Use an original stroke's reveal direction and phase to complement the main subject. Path drawing or an animated mask can implement a line; a shape can move behind another to create occlusion. C01 uses accents after content becomes legible; C07 makes a graphic phrase from occlusion, phase, and a hold. Neither requires a functional metaphor for every stroke.

Keep ornament separate from focus, layout, and data. Let an illustration stop in a composed state. Inspect loop boundaries, including position and velocity continuity when a seamless loop is intended. A short looping asset can still create long-running motion; pause controls and reduced motion depend on the resulting behavior, not the file's duration alone.

### Group assembly and surface handoff

Establish a group or plane before emphasizing inner details when that gives the sequence a clear focal point. Use nested visual layers to separate group travel, inner reveal, hover, and layout responsibilities. C04's tile cluster and C08's overlapping section surfaces are useful examples. Do not let multiple systems overwrite the same layer's transform.

An overlap needs a deliberate stacking and clipping model. Check the previous section's exit, the next section's entry, focus outlines, sticky navigation, and the final reading order. Native scrolling with coordinated surfaces may achieve the desired richness without a custom scroll engine. A presentation's rotating tablet or page sheet is not evidence that these effects belong in the live interface.

## 6. Preserve control and state truth

Design interruptions as transitions with their own meaningful result. Retarget or reverse from the current visible state where feasible; do not jump to an assumed endpoint first. Cancel stale timelines and stale completion callbacks. A newer user intent must not be overwritten by an older animation or network response. Handle resize, route exit, asset failure, and a change of motion preference during the sequence.

Distinguish pending, optimistic, confirmed, and failed state. Optimism is a product decision with a recovery path, not permission to label a timer “saved.” Keep meaningful feedback available even if decorative media is absent. Never make animation completion the only path to enabling a button, exposing content, or releasing a page overlay.

Keep pointer targets stable and keyboard/touch access equivalent. A focus response can share the hover identity without reproducing every flourish. Provide explicit controls for content hidden behind hover or drag. Navigation and form controls require semantic behavior, not merely a convincing recording.

## 7. Adapt without losing the idea

Preserve the expressive relationship rather than copying desktop geometry. A layered desktop mosaic might become a native mobile rail; a multi-plane hero might become two composed scenes; a large shared-image zoom might become direct image continuity with less travel. Do not assume small screens must lose all personality.

Reduced motion is a separate composition: keep the information, selected object, hierarchy, and action while replacing unnecessary spatial travel, camera motion, or loops with stable states or a suitable brief fade. Preference changes must leave the interface usable immediately. Also support applicable pause/stop/hide controls. WCAG SC 2.2.2 is Level A with separate movement and auto-update conditions; SC 2.3.3 is AAA. See R6/R7 and [performance and accessibility](performance-and-accessibility.md).

Reserve media space and use a coherent fallback crop. If assets, scripts, or enhancement APIs fail, ordinary content and navigation must remain available. Rich motion is progressive enhancement unless the requested product itself is a motion experience, in which case define an explicit accessible alternative.

## 8. Judge the result through time

Inspect the whole phrase at normal speed, then onset, overlap, crossing, maximum occlusion, first readability, input readiness, and settlement. Use slow inspection to diagnose, not to decide whether the pace feels right. Check the first use and several rapid repetitions. Test reversal, new selection, late response, skipped entry, route return, and preference changes. Verify loop seams when loops matter.

Review both visual and behavioral outcomes: appealing rhythm, focal hierarchy, readable intermediate states, exact crop continuity, coherent motion vocabulary, stable targets, correct semantics, and truthful state. Measure performance where it matters. Transform and opacity are often useful choices, but masks, large textures, layer count, and decoding still need inspection. Do not infer production smoothness from a file's frame rate or a passing build.

Use [QA and debugging](qa-and-debugging.md) to record executed conditions. Keep reference analysis, written specification, rendered implementation, interaction testing, and human feedback distinct. Sampled source frames can support choreography observations; they do not establish continuous smoothness or the designer's intention. A beautiful result and a reliable interaction both require seeing what actually happens.
