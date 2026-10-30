# Web Motion Director Research Register

**Original research date:** 2026-09-21

**Original version:** 1.0.0; subsequent updates are dated below.

This is a historical evidence register. Apply the current core workflow when earlier source language conflicts with later owner direction, especially the 30 October refinement allowing beauty and enjoyment as sufficient motion intentions. Historical project guidance is not a hidden dependency on an unavailable `DESIGN.md`.

This register records the sources used to shape the skill. The purpose of the research was not to collect fashionable effects. It was to extract repeatable principles for deciding when motion belongs in a web experience, how to implement it safely, and how to verify it.

## Contents

- [Research conclusions](#research-conclusions)
- [Primary and authoritative sources](#primary-and-authoritative-sources)
- [Case studies and practitioner evidence](#recent-case-studies-and-practitioner-evidence)
- [Project-specific rules](#project-specific-design-rules-incorporated)
- [Technology selection](#technology-selection-findings)
- [Anti-patterns](#anti-patterns-identified-during-research)
- [Research limitations](#research-limitations)
- [Joint UI and motion update](#30-october-2026-joint-ui-and-motion-design)
- [Motion principles research](#30-october-2026-motion-principles-research)

## Research conclusions

The strongest common finding is that effective web motion is contextual. Motion should communicate state, continuity, hierarchy, feedback, spatial relationships, narrative progression, or brand character. A technically impressive transition can still be worse than a simple one if it competes with the content.

Recent creative-development case studies also show a consistent pattern: teams often begin with richer effects and then remove or simplify them when the effect distracts from the product. The skill therefore treats restraint as an active design decision rather than a failure to animate.

The second major finding is architectural. Scroll-linked and route-level motion must be treated as systems with lifecycle, interruption, measurement, cleanup, responsive behavior, and reduced-motion alternatives. A collection of isolated tweens is not a motion system.

The third major finding is verification. Animation is temporal, so a static screenshot or a successful build cannot establish correctness. Motion must be sampled or observed through time and across input, viewport, route, and reduced-motion states.

## Primary and authoritative sources

### R1. Nielsen Norman Group, The Role of Animation and Motion in UX
URL: https://www.nngroup.com/articles/animation-purpose-ux/

Used for the principle that motion should support feedback, state changes, navigation metaphors, signifiers, and other clear UX functions rather than exist as decoration.

### R2. OpenAI Academy, Using skills
URL: https://openai.com/academy/skills/

Used for the skill packaging concept, including a reusable `SKILL.md` workflow with supporting resources, examples, and code.

### R3. OpenAI Help Center, Skills in ChatGPT
URL: https://help.openai.com/en/articles/20001066

Used for current ChatGPT skill behavior and the distinction between reusable workflow instructions and host capabilities.

### R4. MDN, View Transition API
URL: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API

Used for same-document and cross-document transition guidance and the principle of preserving context between views.

### R5. web.dev, How to create high-performance CSS animations
URL: https://web.dev/articles/animations-guide

Used for performance guidance: prefer transform and opacity where practical, inspect rendering costs, and use `will-change` sparingly.

### R6. W3C, Understanding Success Criterion 2.3.3: Animation from Interactions
URL: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions

Used for the Level AAA ability to disable nonessential interaction-triggered animation and the documented vestibular risks. Respecting reduced-motion preferences is also a design standard of this skill, not a claim that this particular criterion is AA.

### R7. W3C, Understanding Success Criterion 2.2.2: Pause, Stop, Hide
URL: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide

Used for the Level A control requirements for qualifying movement and automatic updates. The more-than-five-second condition belongs to the moving/blinking/scrolling branch; automatic updates have no five-second exception and may allow frequency control. Apply the criterion's separate conditions and essential exceptions.

### R8. MDN, View Transition API
URL: https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API

Used specifically for the route and state-transition technology matrix.

### R9. MDN, CSS scroll-driven animations
URL: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations

Used for native scroll-linked animation as an option when browser support and complexity fit the task.

### R10. GSAP documentation, ScrollTrigger
URL: https://gsap.com/docs/v3/Plugins/ScrollTrigger/

Used for scroll pinning, scrubbed timelines, horizontal container animation, nested trigger constraints, and scroll measurement patterns.

### R11. GSAP documentation, ScrollTrigger containerAnimation
URL: https://gsap.com/docs/v3/Plugins/ScrollTrigger/

Used for the bounded vertical-to-horizontal chapter pattern. The documentation notes that a horizontally moving container animation can be monitored by nested ScrollTriggers and documents restrictions such as linear easing for the container animation.

### R12. GSAP documentation, gsap.matchMedia()
URL: https://gsap.com/docs/v3/GSAP/gsap.matchMedia()/

Used for breakpoint-specific and `prefers-reduced-motion` animation setup with automatic reversion of created animations and ScrollTriggers.

### R13. GSAP documentation, Flip
URL: https://gsap.com/docs/v3/Plugins/Flip/

Used for shared-element and layout-transition concepts where an element changes position, size, or DOM context.

## Recent case studies and practitioner evidence

The following sources are practitioner case studies. They are used as design evidence and inspiration, not as universal standards.

### R14. Codrops, Podium: Building a Website Where Running Becomes Storytelling
URL: https://tympanus.net/codrops/2026/06/23/podium-building-a-website-where-running-becomes-storytelling/

Key lesson: the selected image or video becomes the transition object from project listing to detail hero. The team rejected a heavier pixel-style transition because it distracted from the media. This strongly supports content-led continuity over decorative transition overlays.

### R15. Codrops, The Never Ending Story: Building a Seamless Infinite Scroll Experience with GSAP & Lenis
URL: https://tympanus.net/codrops/2026/05/28/the-never-ending-story-building-a-seamless-infinite-scroll-experience-with-gsap-lenis/

Key lesson: motion can make a minimal experience memorable when the interaction model itself is deliberate. The implementation combines looping, parallax, and snap control around a clear continuous-gallery concept rather than adding unrelated reveals.

### R16. Codrops, Case Study: Dondre Green
URL: https://tympanus.net/codrops/2025/01/07/case-study-dondre-green/

Key lesson: scroll can reorganize existing visual relationships. The hero title changes role, imagery moves into focus, a section title becomes pinned, and the page progresses into later content. The transition and scroll system are tied to the portfolio’s photography language.

### R17. Codrops, The Spark: Engineering an Immersive, Story-First Web Experience
URL: https://tympanus.net/codrops/2026/01/09/the-spark-engineering-an-immersive-story-first-web-experience/

Key lesson: immersive work should be storyboarded around narrative beats before choosing tools. The project assigns different scroll ranges to different scenes and keeps only one heavy scene active at a time to manage performance.

### R18. Codrops, More Than a Portfolio: Building a Scroll-Driven 3D World with Something to Say
URL: https://tympanus.net/codrops/2026/04/28/more-than-a-portfolio-building-a-scroll-driven-3d-world-with-something-to-say/

Key lesson: 3D is justified when the site is meant to behave like a place or spatial experience. The technology serves the author’s narrative goal, not a generic desire for spectacle.

### R19. Codrops, Building the Maxima Therapy Website: React, GSAP, and Dabbling with AI
URL: https://tympanus.net/codrops/2026/04/06/building-the-maxima-therapy-website-react-gsap-and-dabbling-with-ai/

Key lesson: playful motion can be appropriate even in a healthcare-adjacent context when it follows the organization’s warm, illustrated identity. The implementation combines direct interaction, morphing controls, and ScrollTrigger rather than relying on one repeated reveal.

### R20. Codrops, Building an Infinite GSAP Scroll Gallery with Parallax and Flip Transitions
URL: https://tympanus.net/codrops/2026/07/30/building-an-infinite-gsap-scroll-gallery-with-parallax-and-flip-transitions/

Key lesson: a gallery item can transition into detail through spatial continuity. GSAP Flip records one state and animates to another, including cases where different DOM elements share a transition identity.

### R21. Codrops, Building a Scroll-Revealed WebGL Gallery with GSAP, Three.js, Astro and Barba.js
URL: https://tympanus.net/codrops/2026/02/02/building-a-scroll-revealed-webgl-gallery-with-gsap-three-js-astro-and-barba-js/

Key lesson: custom routing and transition layers can support complex persistent media experiences, but the underlying links remain real navigations. The skill treats such routing layers as specialized solutions, not defaults.

### R22. Codrops, Ten Years Away: Designing an Interactive Comic for Studio375’s Tenth Anniversary
URL: https://tympanus.net/codrops/2026/07/08/ten-years-away-designing-an-interactive-comic-for-studio375s-tenth-anniversary/

Key lesson: scroll velocity, shader response, chapter assembly, and camera movement can all reinforce a specific narrative concept. These patterns belong in immersive storytelling, not ordinary product pages by default.

## Project-specific design rules incorporated

The supplied `DESIGN.md` was treated as a governing design source. In particular, the skill incorporates these rules:

- motion must communicate state, continuity, hierarchy, feedback, narrative, or product behavior;
- do not animate every viewport entrance;
- vertical scrolling is the safe baseline, while horizontal rails, sticky scrollytelling, and snapping are appropriate only when the content relationship justifies them;
- avoid scroll hijacking and trapped pinned sections;
- define reduced-motion behavior;
- responsive design is recomposition, not shrinkage;
- visual QA requires rendering and inspection;
- major directions should be explored divergently before committing.

## Technology selection findings

The research supports a layered technology strategy rather than one universal animation library:

1. CSS transitions and keyframes remain the lowest-cost solution for simple state changes.
2. The Web Animations API is useful for cancellable, programmatic vanilla-JavaScript animation.
3. The View Transition API is a strong option for state and route continuity when browser support and architecture fit.
4. CSS scroll-driven animation can remove JavaScript for straightforward scroll-linked effects where support is acceptable.
5. Motion is a good fit for React presence, layout, drag, spring, and component-scoped motion.
6. GSAP and ScrollTrigger are appropriate for complex choreography, measurement, pinning, scrubbing, SVG, and shared layout transitions.
7. Three.js or React Three Fiber should be reserved for actual 3D, shader, camera, or spatial requirements.
8. Smooth-scroll libraries should not be stacked. If one is used, it must have a clear ownership model and be integrated with any scroll-trigger system.

## Anti-patterns identified during research

The skill explicitly protects against these common failures:

- universal fade-up-on-scroll;
- decorative parallax without a content role;
- forcing horizontal reading of ordinary body copy;
- page transitions that delay navigation without preserving context;
- multiple smooth-scroll systems fighting each other;
- React animation instances that survive unmounts;
- animation that only works with a mouse;
- full desktop scroll choreography copied onto mobile;
- reduced-motion mode implemented as nearly zero-duration spatial motion rather than a genuine alternative;
- permanent `will-change` on many elements;
- WebGL scenes kept active when off-screen;
- a static screenshot treated as proof of the original site’s animation.

## Research limitations

- Practitioner case studies describe individual projects and are not controlled usability studies.
- Browser APIs and support levels can change, so compatibility must be checked when implementing a real project.
- The skill does not encode a fixed visual style. Its purpose is to improve motion reasoning, not to reproduce any referenced site’s recognizable identity.

## 30 October 2026: joint UI and motion design

Version 1.1.0 responds to the owner's request to coordinate this skill with [Graphic Design](https://github.com/MikeyNu/agent-graphic-designer). The refinement is owner direction and original design synthesis. It allows beauty, atmosphere, play, and enjoyment as sufficient intentions, replaces a blanket preference for the smallest effect, and requires early shared composition/sequence work. These instructions refine earlier restrictive language about decoration; they do not claim that the historical sources empirically validated every expressive choice.

The graphic-design repository records the owner's second still-image set: 20 uploads, 19 distinct images, plus observations and proposed motion opportunities. No motion videos had been supplied at that stage, version 1.1.0. The subsequent video study below adds temporal evidence with its own limits. Exact source easing, animation technology, and human response remain unknown.

Direct publisher retrieval on 30 October 2026 rechecked R5 rendering guidance, R6's criterion/level, and R7's separate movement/update conditions. Search-service attempts returned errors, but direct retrieval and relevant text inspection succeeded. This targeted check does not refresh every historical source or establish current library/browser compatibility. Implementation work must verify the APIs it actually uses.

## 30 October 2026: motion principles research

Version 1.2.0 adds [Motion principles and choreography](references/motion-principles-and-choreography.md). The following sources were consulted on 30 October 2026. Platform recommendations, technical documentation, empirical findings, and our design synthesis have different authority. No source establishes one ideal duration, one aesthetic, or the implementation of the owner's clips.

### R23. Carbon Design System, Motion
URL: https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview

Official design-system guidance, page updated 12 August 2026. Supports differentiating productive/expressive moments, coordinating components at page level, and considering travel and size when choosing timing. Its entrance, exit, and visible-to-visible guidance includes contextual exceptions. Exact curves, durations, and IBM's restrictions on ornament are scoped design choices, not universal laws. Text inspected; interactive examples were not played.

### R24. Material Design 3, Motion
URL: https://m3.material.io/styles/motion
API corroboration: https://developer.android.com/reference/kotlin/androidx/compose/material3/MotionScheme

Official platform guidance distinguishes standard/expressive spring schemes and spatial/effects tokens. It supports separating spatial overshoot from color/opacity changes. Springs have stiffness, damping, and initial velocity; visible bounce is not inherent to every spring response. Official indexed text and API documentation were inspected because the direct design page required JavaScript. Embedded demonstrations were not played. Native token details do not establish arbitrary web-library semantics or a requirement to use Material styling.

### R25. Apple Human Interface Guidelines, Motion
URL: https://developer.apple.com/design/human-interface-guidelines/motion

Official guidance supports predictable directional feedback, brief response to frequent input, optional motion, and cancellation without waiting for completion. Official indexed text was inspected; the direct page returned a JavaScript shell. Platform-specific game and immersive guidance is not automatically a web requirement. These recommendations do not prohibit expressive visual art direction.

### R26. Android Developers, Quick guide to Animations in Compose
URL: https://developer.android.com/develop/ui/compose/animation/quick-guide

Primary implementation documentation. Relevant sections distinguish spring, tween, keyframes, sequential/concurrent animation, shared transition state, and re-entry behavior. It describes Compose spring interruption using current velocity. Inspected text, not executed native examples. This supports the model distinction; other frameworks' cancellation and velocity semantics must be checked independently.

### R27. Heer and Robertson, Animated Transitions in Statistical Data Graphics
Author page: https://idl.uw.edu/papers/animated-transitions
Paper: https://idl.cs.washington.edu/files/2007-AnimatedTransitions-InfoVis.pdf

IEEE TVCG / InfoVis, 2007. Abstract, experimental descriptions, discussion, and conclusion were inspected. Two experiments with 24 participants compared static, animated, and staged transitions for object tracking and change estimation. Animation helped in the examined tasks; simple staging had benefits, while some complex staging increased error. These results concern specific chart transitions, not marketing conversion, every UI, or a universal timing scale. No independent replication was performed.

### R28. Nielsen Norman Group, Executing UX Animations: Duration and Motion Characteristics
URL: https://www.nngroup.com/articles/animation-duration/

Page Laubheimer, 9 February 2020. Practitioner guidance helps distinguish trigger, changing properties, duration, and easing, with duration considered in context. Inspected article text. Treat numerical recommendations as design starting points, not a measured law for every distance, device, or repeated task.

### Targeted refresh of existing technical sources

R5's rendering guidance and R6/R7's separate accessibility scopes were rechecked at their official URLs. R9's current MDN guide, https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations, distinguishes elapsed-time and scroll/view progress timelines. Text inspection supports the mechanism distinction; it does not establish current support across a project's target browsers. Refresh APIs and compatibility when implementing.

### Owner clips and original synthesis

The companion's [nine-clip study](https://github.com/MikeyNu/agent-graphic-designer/blob/main/skills/graphic-design/references/owner-motion-study.md) records file hashes, nominal metadata, timestamps, close observations, interpretations, plausible constructions, and adaptation limits. The 199 overview selections, 395 dense selections across 26 windows, and seven detail crops were inspected. Continuous normal-speed playback, audio, source code, live controls, actual device performance, and participant reactions were not evaluated.

The four-clock distinction, readable/usable/settled milestones, construction recipes, creative critique, and transfer exercises are original synthesis. The clips support observed relationships such as masks, overlap, object continuity, and coordinated progress; they do not prove creator intent, exact easing, a particular library, or general UX efficacy. Beauty and pleasure remain valid intentions without borrowed scientific certainty. No third-party clip or extracted frame is redistributed in the package.

## 30 October 2026: template convergence and motion review

Version 1.2.1 adds [template-choreography guidance](references/graphic-design-coordination.md#prevent-template-choreography) informed by the owner's supplied negative reference, [UI UX Pro Max](https://uupm.cc/). The companion's [study and access record](https://github.com/MikeyNu/agent-graphic-designer/blob/main/skills/graphic-design/references/template-convergence-study.md) covers all 39 published desktop gallery previews, twelve live full-page compositions/section maps, and six displayed prompts. It is a case observation and original critique, not a controlled test of the generator or a claim about all AI-produced interfaces.

Observed evidence includes repeated visual structures across surface styles, task-specific exceptions, two working local prompt/style controls, and one declared 20-second infinite agency marquee. This does not establish gallery-wide motion, perceived smoothness, reduced-motion compliance, integrated functionality, or performance. No source code implementation, mobile behavior, generation, wallet operation, or backend completion was verified.

Comparing lead objects, stable regions, overlap, repetition, and settlement across design alternatives is our synthesis. Distinguishing a demo from live state and maintaining within-product consistency refine the existing contract. The update does not prescribe a new default aesthetic, prohibit ornament, or claim that style names reveal authorship. Runtime helpers and dependencies are unchanged.

## 31 October 2026: QA and lifecycle refresh

R29. MDN [pagehide](https://developer.mozilla.org/en-US/docs/Web/API/Window/pagehide_event) and [pageshow](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageshow_event), consulted for retained-page lifecycle behavior. A page may return from the back/forward cache; a `pagehide` handler does not prevent that. Page-exit events are not guaranteed on every mobile termination. Persist important drafts during editing, not solely at exit. Documentation establishes event semantics, not the correctness of our examples.

R30. [Playwright Page API](https://playwright.dev/python/docs/api/class-page), consulted for navigation, runtime-error capture, and verification limits. HTTP error responses need explicit status inspection; navigation need not throw. `networkidle` is discouraged for test readiness. The documentation also states that BFCache testing is unsupported and normally disabled. A synthetic lifecycle test or ordinary automated Back action is not evidence of actual cache restoration. Recheck the tool version when applying this guidance.

R6/R7 were rechecked for their separate WCAG levels and conditions. R14 was re-opened at its original practitioner source. This targeted refresh does not revalidate every historical source or establish current browser compatibility.

Version 1.2.2 adds task routing, bounded evidence claims, source-helper regressions, and suspension/return checks. A queue exercise exposed a close-state guard left active after cancellation on `pagehide`. The corrected handlers pass isolated logic checks; real browser restoration is NOT RUN. The instruction to settle or deliberately resume transient UI state is engineering synthesis from that defect and the documented lifecycle. See [the validation record](../../VALIDATION-2026-10-31-QA.md).
