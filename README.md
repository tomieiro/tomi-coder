# tomi-coder

Three skills for developing in the Tomi style: concrete domain parts, direct implementation, incremental integration, and later review. **Always use TDD: write the test first, observe RED, reach GREEN, then refactor.**

[BASE](BASE.md) was inferred from six example repositories and their commit histories. The [evidence report](docs/style-and-evidence.md) distinguishes observations from assumptions; the history does not establish systematic TDD. The [provenance record](docs/code-provenance.md) identifies selected source revisions, authorship checks, and adaptations. The original example clones were removed after extraction at the user's request.

## The three stages

| Skill | Responsibility | Output |
| --- | --- | --- |
| [tomi-coder-prepare](skills/tomi-coder-prepare/SKILL.md) | Read existing work, select environment/build/runner, prepare minimal structure, and write tests first. | Contract, commands, required stubs, and observed RED. |
| [tomi-coder-develop](skills/tomi-coder-develop/SKILL.md) | Implement new capabilities through BASE and edit existing code with Ponytail-inspired restraint. | Working slices, GREEN, and affected regression checks. |
| [tomi-code-construct](skills/tomi-code-construct/SKILL.md) | Review simplicity, modularity, BASE alignment, failures, and security; fix with TDD and build. | Inspected local result, verification, and explicit limits. |

The third name is intentionally **`tomi-code-construct`**. BASE is a shared reference, not a fourth skill. A human development style allows incremental refinement; it does not call for deliberate bugs or postponing a known vulnerability.

The skills include [anonymized code examples](skills/tomi-coder-develop/references/code-examples.md) for state, operations, reuse, logic, callbacks, and navigation, a [TDD preparation example](skills/tomi-coder-prepare/references/tdd-example.md), and a [before-and-after review](skills/tomi-code-construct/references/review-example.md). These examples preserve the source MIT notices while using neutral domain names.

## Use

After installing the skills, requests can look like this:

```text
Use $tomi-coder-prepare to prepare a CSV expense grouping script.
Use $tomi-coder-develop to implement the prepared slice and turn the tests green.
Use $tomi-code-construct to review, correct, and build the result.
```

Request all three stages for a complete cycle. They proceed without routine confirmation between stages. If only preparation is requested, red tests are the expected output. A stage invoked alone reconstructs its missing prerequisites.

Each skill folder is self-contained: it includes its own BASE copy, references, and applicable license notices. Copy the complete folder into your agent's skill directory. For Codex, use `$CODEX_HOME/skills` when set or `~/.codex/skills` otherwise. Preserve any existing installation before replacing it. This repository does not alter the agent installation automatically.

Tool selection follows evidence: preserve the existing chain, prefer native resources, verify commands, and distinguish environments, dependencies, tests, builds, and execution. Make, Gradle, and micromamba are conditional options. Investigate an unknown name such as `riema` rather than inventing its commands.

## Maintain and verify

Edit only the canonical root `BASE.md` and sync its exact copies before distributing. Python 3 is sufficient; GNU Make is optional:

```sh
python3 scripts/sync_base.py --write
python3 -m unittest discover -s tests -v
python3 scripts/sync_base.py
```

Alternatively run `make sync-base` and `make check`. Without `--write`, the sync command is read-only and exits with code 1 if a copy is missing or different. Four tests check copying, drift detection, missing input, and CLI exit codes. Eight further tests extract code from Markdown and exercise it with Lua, GCC, G++, and the JDK; they include the preparation example's RED → GREEN cycle. Missing tools produce explicit skips. Full validation requires all four language tools and no skips. Execution uses temporary directories, not the original clones.

If the `skill-creator` skill is available, also run its `scripts/quick_validate.py` for each skill. That checks skill structure, not future agent decisions.

Review instruction changes against these scenarios:

| Scenario | Expected behavior |
| --- | --- |
| Empty app | Test before functional source; minimal bootstrap; RED before development. |
| Legacy bug without tests | Characterize preserved behavior and reproduce the defect before correction. |
| Missing runner or SDK | Record a blocker; do not count environment failure as RED or claim GREEN. |
| Behavior-preserving refactor | Characterization may start green; preserve behavior. |
| Script without compilation | Run tests and execution smoke checks without inventing a build. |
| Finding during construct | Regression first, then correction and rebuild of invalidated artifacts. |
| Review-only request | Findings and proposed fixes without edits. |
| New module versus local edit | BASE guides decomposition; Ponytail guides economy while preserving TDD. |

These are review criteria, not a claim that agents have exercised every environment. No deployment, commit, push, or global installation is implicit in the skills.

## Derivation and licenses

The repository retains its [Apache-2.0 license](LICENSE). `tomi-coder-develop` includes an adaptation of [Ponytail by DietrichGebert](https://github.com/DietrichGebert/ponytail), originally under MIT. The [adaptation](skills/tomi-coder-develop/references/ponytail.md) is based on `skills/ponytail/SKILL.md` at revision `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`. Its original **Copyright (c) 2026 DietrichGebert** and MIT terms are preserved in [PONYTAIL-LICENSE](skills/tomi-coder-develop/references/PONYTAIL-LICENSE). The adaptation mandates TDD even for small behavior changes and keeps BASE's domain decomposition. The original Ponytail does not need to be installed.

BASE is an original synthesis of observations. The code references are attributed derivatives of selected MIT material, with changes recorded in the provenance document. Each skill carries an `EXAMPLES-LICENSE` notice: [prepare](skills/tomi-coder-prepare/references/EXAMPLES-LICENSE), [develop](skills/tomi-coder-develop/references/EXAMPLES-LICENSE), and [construct](skills/tomi-code-construct/references/EXAMPLES-LICENSE). Preserve these notices when redistributing snippets. The root Apache-2.0 license does not replace the MIT notices. No LicensePicker source was reused because its application license could not be established.
