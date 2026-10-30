# Web Motion Director

Web Motion Director is a reusable ChatGPT skill for intentional motion design and implementation in websites and web applications.

It addresses a common failure mode in AI-generated frontend work: an interface may be visually competent at rest but remain completely static, or animation may be added later as generic fade-up effects. This skill inserts motion reasoning into the design and implementation process itself.

## What it does

The skill teaches an agent to:

- inspect the product, audience, design system, codebase, and references;
- decide whether a region should remain static or use feedback, spatial, scroll-linked, narrative, or immersive motion;
- infer plausible motion from a static reference without pretending the screenshot proves the original animation;
- study temporal references with timestamped observations and separate interface motion from presentation editing;
- compose staging, overlap, holds, masks, type, and shared imagery with explicit state and interruption;
- create a product-specific motion thesis;
- explore multiple motion directions before committing on major work;
- design navigation, menu, route, microinteraction, and scroll choreography;
- implement bounded vertical-to-horizontal sections that return to normal vertical flow;
- choose CSS, Web Animations API, View Transitions, Motion, GSAP, or 3D based on the actual motion problem;
- create separate responsive and reduced-motion behavior;
- preserve keyboard, focus, semantic navigation, and performance;
- verify animation through time in a rendered browser.

## Important behavior

The skill designs appearance and motion together, with room for beauty, play, atmosphere, and enjoyment as well as functional response. Quiet regions can support expressive moments. Neither maximum movement nor the smallest possible effect is a universal goal.

A static screenshot is treated as evidence of composition only. If no temporal reference exists, any added motion is explicitly a design proposal.

## Source map

- `SKILL.md`: primary agent workflow
- `references/`: motion strategy, scrolling, navigation, responsive, accessibility, performance, QA, and case-study guidance
- `references/graphic-design-coordination.md`: joint visual/temporal design, shared contracts, early prototyping, and reference evidence
- `references/motion-principles-and-choreography.md`: researched principles, sequence scoring, motion models, and practical visual construction
- `scripts/motionctl.py`: conservative static motion-risk and plan helper
- `scripts/browser_motion_audit.py`: optional Playwright temporal sampling helper
- `RESEARCH.md`: research register
- `CHATGPT_PROJECT_INSTRUCTIONS.md`: compact project instruction bridge
- `INSTALL.md`: installation and use guidance
- `agents/openai.yaml`: host metadata

The downloadable v1.0.0 package may include additional validation and evaluation artifacts. This repository keeps the reusable source clean and excludes generated screenshots, bytecode, caches, and other test evidence.

## Relationship to design systems

Web Motion Director is designed to work under a project's existing `DESIGN.md`, component library, architecture, and CI workflow. It does not impose a single visual style or animation library.

## Relationship to Graphic Design

Use [Graphic Design](https://github.com/MikeyNu/agent-graphic-designer) alongside this skill when creating or redesigning an interface. Follow [the coordination guide](references/graphic-design-coordination.md): compose and prototype together, share one brief, and let playback inform the layout. It is an optional companion, not a hidden runtime dependency or a requirement to use multiple agents.

The 30 October 2026 updates establish this joint workflow and align the skills' treatment of aesthetic pleasure. The graphic-design repository now holds studies of 39 distinct still references and [nine motion clips](https://github.com/MikeyNu/agent-graphic-designer/blob/main/skills/graphic-design/references/owner-motion-study.md). The clip study uses timestamped frame samples and detailed crops, with explicit limits on playback, trigger, and implementation certainty. Version 1.2.0 applies these observations alongside primary motion guidance and research.

## Relationship to Visual Asset Pipeline

The two skills are complementary:

- **Visual Asset Pipeline** reasons about and delivers generated or recovered imagery.
- **Web Motion Director** reasons about how interface elements, imagery, navigation, and scroll should behave through time.

For reference-driven website reconstruction, use both when imagery and animation are material to the result.
