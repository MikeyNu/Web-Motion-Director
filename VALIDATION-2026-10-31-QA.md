# Web Motion Director 1.2.2 QA, 31 October 2026

**Follow-up:** the user authorized local desktop-browser testing and confirmed a GitHub billing blocker. The [desktop follow-up](VALIDATION-2026-10-31-DESKTOP.md) records the subsequently executed browser checks. Earlier NOT RUN statements below describe the initial environment, not the later desktop run.

This release strengthens task interpretation, lifecycle recovery, helper contracts, and verification language. The [joint five-case record](https://github.com/MikeyNu/agent-graphic-designer/blob/main/evals/validation-2026-10-31-qa.md) contains the complete exercise method, original findings, and capability limits. It is not evidence that every future agent result will be correct.

## Package and instruction review

Reviewed the core, twelve reference guides, research register, installation/project instructions, manifest, scripts, and optional dependencies. The core now routes repairs, new directions, faithful reconstruction, and handoffs explicitly. Approved direction and requested scope take priority; three new concepts are not mandatory for a correction. Substantial UI/motion work shares one brief, exploration, and prototype with Graphic Design.

Removed a compulsory-seeming intensity ladder for concept selection, separated implementation stage from check status, clarified missing-runtime behavior, and added retained-page leave/return checks. Historical research is labeled as such; current core direction takes precedence over older project-specific restrictions. Beauty and expressive character remain valid intentions. Licenses and optional-dependency boundaries are preserved.

## Reproduced helper issues and repairs

| Helper | Before | After and evidence |
| --- | --- | --- |
| Source scan | Missing/empty paths could return zero files without a meaningful failure; skipped sources were not reliably distinguished. | Missing/no-source input fails; unreadable, oversized, and symlink source files are explicit; discovery prunes dependency/build trees; found/scanned/skipped counts are distinct. A successful heuristic scan says REVIEW, not motion PASS. |
| Plan validator | Presence of top-level keys could accept empty/wrongly typed content. | Validates root/type/nonempty requirements, intent IDs and uniqueness, known postures, and required intent descriptions. A deliberate static thesis may have no intents. This is structural validation, not a design-quality judge. |
| Tag extraction | Malformed or unsupported literal tags could be missed or produce misleading data. | Rejects malformed JSON, non-object payloads, unmatched and nested tags; valid objects and genuine absence remain distinct. Literal syntax and limits are documented. |
| Browser sampler | Local content lost its document base, requested scroll was conflated with actual position, runtime errors and some navigation failures were weakly reported. | Navigates to the authorized document URL, remeasures growing extent, records requested/actual scroll, captures page/console errors, rejects HTTP error pages, cleans up contexts, and protects old evidence from overwrite. |
| Browser evidence | Capturing static positions could be read as animation QA. | CAPTURED describes successful capture only. Reports and docs exclude normal-speed playback, interaction, accessibility conformance, and performance claims. All sampler checks in this review use fake objects. |

The sampler's fixed 250 ms pause is not a page-readiness assertion. Its active-animation count is not FPS. It is optional and usable only when the host permits its runtime and target. No local browser execution or policy workaround occurred in this QA.

## Executed tests

```sh
python3 -m unittest discover -s tests -v
node evals/qa-2026-10-31/verify.cjs
```

- **PASS: 27 repository tests.** Twenty-two offline helper regressions and five package contracts cover invalid inputs, pruning, counts, heuristic risk signals, tag/plan validation, fake sampler navigation/error/cleanup behavior, output protection, core size/frontmatter, version agreement, local Markdown links/fragments, portability, and both original MIT notices.
- **PASS: package validator and diff checks.** Standard name/description frontmatter, compact core, consistent 1.2.2 version, no introduced machine paths or em dashes in instructions, unchanged licenses, and clean whitespace.
- **PASS: 15 source/isolated checks on the fresh motion repair.** The [retained fixture, output, and harness](evals/qa-2026-10-31/README.md) preserve approved styling while testing immediate state, reversal, stale callbacks, reduced motion, conditional focus calls, optional-animation failure, missing completion, page exit, and 1,000 rapid toggles.
- **PASS with bounded evidence: companion queue repair.** A source review found a closing guard stranded after persisted `pagehide`; the corrected helpers pass seven isolated lifecycle checks. Actual cache restoration remains NOT RUN. The initial failure is retained in the joint record.

CI configuration runs the Python suite on pushes and pull requests. The results above are locally executed evidence; a configured workflow is not a completed hosted run. The companion's 45 repository tests bring the two-package total to 72. Do not combine that count with browser verification or treat each assertion as an independent design trial.

After publication, [GitHub run 41146233823](https://github.com/MikeyNu/Web-Motion-Director/actions/runs/41146233823) reported failure before any test steps. No runner was assigned and no job log was available. Check annotations were unavailable through the connector, so the cause is unconfirmed. The companion's new hosted run also failed before test steps, and its preceding revision already had a failed run. Hosted CI is not passing; investigate the run details before claiming hosted execution. The published source tree matches the locally tested version.

## Limits

The allowed browser preview rejected the local target and prohibited alternate routes. Browser layout, actual keyboard/Tab/focus, native dialog/history behavior, real BFCache restoration, screen readers, normal-speed animation, temporal frames, device tests, and measured performance are **NOT RUN**. The corrected HTML is a review prototype with source/logic evidence, not a production-readiness claim. Fresh exercises demonstrate scoped transfer, not statistical reliability or infallibility.

Primary documentation refreshed for this review is recorded in [RESEARCH.md](skills/web-motion-director/RESEARCH.md#31-october-2026-qa-and-lifecycle-refresh). Historical references retain their original dates and limitations. No third-party reference clips, screenshots, fonts, or site assets are redistributed.
