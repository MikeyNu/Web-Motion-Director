# Web Motion Director Research Register

**Research date:** 2026-09-21  
**Version:** 1.0.0

This register records the sources used to shape the skill. The purpose of the research was not to collect fashionable effects. It was to extract repeatable principles for deciding when motion belongs in a web experience, how to implement it safely, and how to verify it.

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

Used for reduced-motion requirements and the documented vestibular risks of unnecessary motion triggered by interaction or scrolling.

### R7. W3C, Understanding Success Criterion 2.2.2: Pause, Stop, Hide
URL: https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide

Used for continuously moving, blinking, scrolling, or auto-updating content that runs for more than five seconds alongside other content.

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

Key lesson: immersive work should be storyboarded around narrative beats before choosing tools. The project assigns different scroll ranges to different scenes and keeps only one heavy lscene active at a time to manage performance.

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
