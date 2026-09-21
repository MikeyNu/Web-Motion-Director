# Motion pattern library

These are patterns, not prescriptions. Select them from product needs.

## 1. Shared media handoff

**Use when:** a media object is the user’s selection and remains important on the destination page.

**Behavior:** preserve or simulate the object’s current geometry, route underneath, then settle it into the destination hero.

**Good for:** portfolios, commerce, editorial collections.

**Avoid when:** source and destination objects are unrelated, or the transition delays a frequent task.

## 2. Role-changing hero object

**Use when:** a hero element can become a persistent navigation or chapter anchor.

**Behavior:** resize/reposition the object as the user leaves the hero, then keep it stable while later content takes focus.

**Good for:** editorial, portfolio, branded marketing.

**Risk:** layout complexity and collision on mobile.

## 3. Bounded horizontal chapter

**Use when:** a finite set has meaningful lateral order and benefits from simultaneous visual continuity.

**Behavior:** native vertical input drives an inner horizontal track while the chapter frame remains stable, then normal flow resumes.

**Good for:** case studies, capability sequences, timelines, product families, image-led portfolios.

**Avoid when:** the content is mostly long text, forms, tables, or users need rapid scanning.

## 4. Sticky visual explanation

**Use when:** one diagram, product image, or mockup needs to change as explanatory steps progress.

**Behavior:** visual remains sticky, copy progresses, and the visual changes state at defined chapters.

**Good for:** product demonstrations, architecture explanations, education.

## 5. Mask or aperture reveal

**Use when:** a brand’s shape language naturally supports revealing media or routes.

**Behavior:** a clip/mask expands or contracts from a meaningful origin.

**Avoid when:** it is an arbitrary circle wipe added to a product with no related identity.

## 6. Focus-through-depth gallery

**Use when:** multiple media items pass through a primary inspection zone.

**Behavior:** center item gains clarity/scale while peripheral items soften or recede.

**Good for:** photography and visual portfolios.

**Risk:** blur can be expensive and visually distracting. Use restrained values and reduced-motion fallback.

## 7. Spatial drawer or panel

**Use when:** a secondary task is related to the current context.

**Behavior:** panel enters from a direction that communicates attachment to its trigger or edge; background stays stable.

**Good for:** admin, commerce, filters, record details.

## 8. Layout reflow continuity

**Use when:** filtering, sorting, expanding, or changing view modes reorganizes existing items.

**Behavior:** items move from previous to new positions instead of disappearing and reappearing.

**Good for:** grids, dashboards, catalogues.

## 9. Narrative scene sequence

**Use when:** the experience itself is storytelling.

**Behavior:** user scroll or explicit progress advances a designed scene timeline with clear chapters.

**Good for:** campaigns, immersive portfolios, historical timelines.

**Requirement:** storyboard before selecting implementation technology. [R17]

## 10. Controlled infinite gallery

**Use when:** endless browsing is itself the experience.

**Behavior:** loop feels continuous, orientation remains understandable, and interaction has a consistent rhythm.

**Avoid when:** users need a clear beginning/end, SEO-rich reading, or task completion.

## 11. Morphing control

**Use when:** the control changes role or mode and the shape transition clarifies that transformation.

**Good for:** playful or expressive brands.

**Avoid when:** a straightforward state change would be clearer in high-trust workflows.

## 12. Motion-responsive background

**Use when:** a background can reinforce pace or narrative without competing with content.

**Behavior:** background changes subtly with scroll or pointer velocity.

**Risk:** expensive filters/shaders and vestibular effects. Keep secondary and provide reduced motion.

## 13. Section handoff object

**Use when:** one object crosses the visual boundary between two sections.

**Behavior:** object becomes the continuity bridge while surrounding layout changes.

**Good for:** product storytelling and static designs that already visually overlap sections.

## 14. Menu reveal with geometry

**Use when:** navigation is a meaningful brand surface.

**Behavior:** menu grows from trigger or header geometry, with links following a clear hierarchy.

**Requirement:** interruption, Escape, focus, reduced motion, and scroll-lock cleanup.

## 15. Quiet route transition

**Use when:** context preservation matters but spectacle does not.

**Behavior:** short opacity or clip transition, often with the destination heading or media appearing first.

**Good for:** healthcare, enterprise, content-heavy platforms.
