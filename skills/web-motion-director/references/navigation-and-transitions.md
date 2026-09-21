# Navigation and transitions

## Purpose

Navigation motion should preserve context, clarify hierarchy, or express the brand without delaying access to the destination.

## Transition models

### Shared element

Use when the selected object exists meaningfully in both views. Examples:

- project thumbnail -> project hero;
- product card image -> product gallery;
- article cover -> article header;
- profile avatar -> profile detail.

This is often more coherent than placing an unrelated overlay between routes.

### Directional hierarchy

Use when navigation has a genuine spatial relationship, such as advancing through steps or moving between parent and child views.

Do not invent left/right direction for unrelated top-level pages.

### Brand mask or motif

A logo-derived shape, shutter, aperture, wipe, or other motif can support branded navigation when it is specific to the identity and short enough not to become a loading curtain.

### Minimal crossfade

For high-trust or utility surfaces, a short fade or direct swap may be the strongest choice.

## View Transition API

Consider the View Transition API when:

- browser support meets the target;
- the existing router can participate cleanly;
- the transition benefits from captured old/new states;
- same-origin document or same-document transitions fit the architecture.

Provide a normal navigation fallback. Never break standard links solely to gain animation.

## GSAP Flip

Consider Flip when a real object changes position, size, or DOM hierarchy and spatial continuity matters. Keep stable transition IDs scoped carefully so concurrent objects do not claim the same identity.

## Custom routers and Barba-like layers

Use only when the application architecture genuinely benefits from intercepted page lifecycle and persistent scenes. Do not introduce a second routing system into a mature Next.js or SPA project without architectural justification.

If a custom transition layer is used:

- preserve real URLs and browser history;
- handle direct page entry;
- handle back/forward;
- manage focus after navigation;
- preserve scroll restoration intentionally;
- cancel or finish transitions when navigation changes rapidly;
- ensure errors do not leave the page visually covered.

## Menu motion

A menu should feel connected to its trigger and structure.

Possible patterns:

- clip or mask opens from trigger geometry;
- panel expands from navigation region;
- typography reveals in reading order;
- background and links use different timing hierarchy;
- active route preserves a visual anchor.

Do not stagger every link simply because stagger exists.

### Interruption

Opening and closing must be interruptible. Use reversible or retargetable animation so a second click does not wait for the first timeline.

Semantic state is authoritative:

- `aria-expanded` tracks menu state;
- focus enters the menu at the right moment;
- Escape closes it;
- focus returns to the trigger;
- background interaction is disabled only while appropriate;
- body scroll lock is cleaned up reliably.

## Transition duration

A transition that users encounter repeatedly should generally feel faster than a one-time brand intro. If people can complete the destination task before the transition finishes, the transition is probably too long.

## Loading

Do not hide slow data or image loading behind an elaborate animation and call it performance. Preload only what the destination genuinely needs and surface real loading state when necessary.
