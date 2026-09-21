# Installation and use

## ChatGPT project or conversation

Attach the complete skill package or provide the extracted skill folder where the host can read it. Add `CHATGPT_PROJECT_INSTRUCTIONS.md` to project instructions when useful.

Suggested invocation:

> Use Web Motion Director for this frontend work. Inspect the product, design rules, code, references, and current animation stack. Decide where motion is justified, define a coherent motion direction, implement it with the lightest suitable technology, and verify the actual motion on desktop, mobile, keyboard, and reduced-motion states. Do not add generic animation merely to make the page move.

Attaching files does not grant browser access, repository access, package-install permission, or deployment authorization.

## Skill-capable local environments

OpenAI documents skills as reusable workflows centered on a `SKILL.md` file with optional supporting resources. [R2]

A common repository-level layout is:

```text
<repository>/.agents/skills/web-motion-director/
  SKILL.md
  references/
  scripts/
  templates/
  ...
```

A user-level skill may be placed under the host’s supported user skill directory. Inspect the current host documentation instead of guessing a global path.

## Plugin-bundled source

The companion plugin source package has this shape:

```text
web-motion-director-plugin/
  plugin.json
  README.md
  skills/
    web-motion-director/
      SKILL.md
      ...
```

A source ZIP is not the same thing as an installed plugin. Use the host’s current plugin-development or marketplace workflow.

## Dependencies

The skill itself has no runtime dependency on a particular JavaScript animation library.

Python helper baseline:

```text
Python 3.10+
```

Optional validation dependencies are listed in:

```text
requirements.txt
requirements-optional.txt
```

`browser_motion_audit.py` requires Playwright and a browser installation when used.

## Project integration

Before frontend work, the agent should read:

- applicable `DESIGN.md` and design-system docs;
- repository or `AGENTS.md` instructions;
- architecture and workflow docs;
- package manifests and lockfiles;
- existing animation utilities and libraries;
- relevant routes/components;
- reference images, video, Figma motion, or supplied prototypes.

The skill must not replace a project’s approved CI or repository workflow.

## Upgrades

When upgrading the skill:

1. compare the existing skill package with the new version;
2. preserve project-specific overrides outside the skill folder;
3. rerun package tests;
4. review `RESEARCH.md` for browser/library assumptions that may have changed;
5. do not overwrite local modifications blindly.
