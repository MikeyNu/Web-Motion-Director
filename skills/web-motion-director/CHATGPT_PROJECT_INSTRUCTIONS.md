# Project instruction bridge: Web Motion Director

For substantial frontend design, reconstruction, or polish work, use the attached or installed `web-motion-director` skill unless the task explicitly requires a static experience.

Read the project’s actual design rules, architecture, workflow documents, source, routes, assets, and animation stack before adding motion.

Design appearance and motion together. Beauty, atmosphere, rhythm, play, feedback, continuity, and narrative are valid intentions. Use one shared brief with the available graphic-design skill, following `references/graphic-design-coordination.md`. For major work, explore materially different visual/temporal directions and prototype a principal sequence before fixing the layout. Keep quiet support around expressive regions instead of applying one entrance recipe everywhere.

When a static screenshot or image is the reference, preserve required resting-state fidelity while designing the temporal relationship. Label added motion as a proposal and do not claim that a still image proves original timing, easing, page transitions, hover states, or scroll behavior. For video, inspect normal-speed playback and timestamped events; distinguish interface motion from presentation edits and report playback limits.

Motion should be intentional across navigation, menus, page transitions, microinteractions, and scrolling. Bounded vertical-to-horizontal sections are allowed when the content relationship justifies them: preserve native vertical scroll input, pin only for the chapter, move an inner horizontal track, let users reverse naturally, then return to ordinary vertical flow. Use a different mobile and reduced-motion composition where needed.

Use the lightest suitable implementation. Prefer existing project conventions. Do not add GSAP, Motion, Three.js, a smooth-scroll engine, or a custom router merely because the tool exists. Never run multiple scroll owners without a demonstrated reason.

Respect `prefers-reduced-motion`, keyboard operation, focus, standard links, browser history, direct route entry, and touch behavior. Autoplaying continuous motion must follow applicable accessibility requirements.

Do not claim motion QA from code inspection or a successful build. Inspect actual temporal states in a browser at representative desktop and mobile sizes, test reduced motion, and check interruption/reversal where applicable. Preserve the project’s established Git and CI workflow and report anything that remains unverified.
