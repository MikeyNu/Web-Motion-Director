# Scroll choreography

## Principle

Scrolling is navigation through content. Animation may reinterpret scroll progress, but it must not make the user lose control of the document.

## Default

Use native vertical scrolling unless the content model justifies something else.

## Bounded vertical-to-horizontal section

This is the first-class pattern for a page that scrolls downward, enters a horizontal chapter, then continues downward.

### Structure

```text
normal document flow
  -> horizontal chapter wrapper
      -> stable/pinned viewport frame
      -> inner horizontal track
          -> item 1
          -> item 2
          -> item 3
  -> normal document flow resumes
```

### Measurement

Measure real overflow after layout:

```text
horizontalDistance = max(0, track.scrollWidth - viewportWidth)
```

The vertical scroll range should be derived from content and interaction feel, not a hard-coded arbitrary number that breaks when items change.

### Behavior

- preserve vertical wheel, touch, and keyboard page input;
- map vertical progress to horizontal track translation;
- allow backward scrolling naturally;
- pin only for the bounded chapter;
- unpin cleanly at both ends;
- keep important text readable without requiring sideways reading;
- avoid pinning the same element that is being translated when the implementation library discourages it;
- refresh measurements after fonts and media settle;
- handle resizes without leaving stale transforms.

### Nested triggers

If content inside a horizontally transformed track needs its own reveal or activation points, use the chosen library’s supported container-progress mechanism. GSAP ScrollTrigger provides `containerAnimation` for this case, with documented limitations.

### Mobile

Common mobile transformations:

- vertical stack;
- native horizontal overflow with touch drag and visible affordance;
- smaller finite carousel with buttons and scroll snapping;
- discrete stepping rather than long pinning.

Do not keep a desktop pin solely because the code can technically run on mobile.

### Reduced motion

Render the content in a normal sequence. Do not use a near-zero-duration horizontal translation while retaining the pin.

## Sticky narrative

Use when a stable visual or diagram changes while related copy progresses.

Rules:

- the sticky region must have an obvious end;
- focusable controls inside must remain reachable;
- the user must be able to reverse through the sequence;
- do not hide information exclusively in intermediate scroll states;
- content should still make sense if JavaScript is delayed or disabled where practical;
- mobile may collapse into sequential scenes.

## Scroll-triggered reveals

Intersection-triggered reveals are acceptable when they clarify hierarchy or establish a deliberate rhythm. Do not apply one fade-up preset to every heading, paragraph, and card.

Prefer revealing groups according to content relationships rather than DOM order alone.

## Parallax

Use only when differential depth reinforces the composition. Keep displacement moderate. Large viewport-wide parallax can cause vestibular discomfort and should be removed or greatly reduced in reduced-motion mode.

## Snap

Snap can fit:

- discrete fullscreen scenes;
- a media gallery;
- a finite story sequence;
- situations where intermediate positions are visually meaningless.

Avoid snap for ordinary article copy, forms, dense tables, or long mixed-content pages.

## Smooth scrolling

Native scroll is the baseline. If a smooth-scroll library already exists, inspect its ownership model before adding triggers.

Never run two smooth-scroll engines simultaneously.

If a library uses transformed content, confirm how sticky positioning, fixed elements, anchor links, focus, browser history, and accessibility behave.

## Failure modes

- blank gaps after pinning;
- horizontal overflow outside the intended chapter;
- pinned content obscuring later sections;
- jump when entering or leaving the pin;
- stale dimensions after font/image load;
- triggers firing at wrong locations inside transformed tracks;
- body scroll disabled after component unmount;
- wheel/touch handlers preventing normal navigation;
- scroll progress driving React state every frame and causing jank.
