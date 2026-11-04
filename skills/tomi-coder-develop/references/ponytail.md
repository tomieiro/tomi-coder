# Ponytail adapted to the Tomi workflow

Derived from [Ponytail by DietrichGebert](https://github.com/DietrichGebert/ponytail), `skills/ponytail/SKILL.md`, revision `96608e078b2d5ea607c5c3b8b5a54d1c1fba6846`. Copyright (c) 2026 DietrichGebert. The original MIT notice accompanies this adaptation in [PONYTAIL-LICENSE](PONYTAIL-LICENSE).

This adaptation applies to work under this skill only. It does not activate persistently or require installation of the original Ponytail. BASE, mandatory TDD, and the user's request bound simplification.

## Before simplifying

Understand the actual flow, callers, contracts, and effects. Skipping that reading can put a small change in the wrong place.

Choose the first solution that fully covers the need:

1. Drop only speculative future features.
2. Reuse an existing operation, component, or convention.
3. Use the standard library or a suitable native platform feature.
4. Reuse an installed dependency that solves the problem.
5. Write the smallest readable implementation satisfying the remaining contract.

Avoid unnecessary interfaces, empty wrappers, unused configuration, and architectural layers without a concrete job. Preserve useful existing boundaries. A low file count does not justify mixing UI, persistence, and rules into an untestable module.

For bugs, correct the shared root cause where it belongs. Check consumers and update affected code. Moved code retains validation and error handling. A cryptic one-liner is not a simplification. Document a deliberate limit only when it matters, naming the limit and the condition for changing it.

## Deliberate differences from the source

- TDD applies even to small behavioral changes; the original exemption for trivial changes is not used.
- BASE guides decomposition of new capabilities; file count alone does not.
- No mode may remove an explicit requirement in the name of YAGNI.
- Replies include evidence and limits needed to review the work.

Never remove data protection, access controls, boundary validation, failure handling, or explicit requirements to shorten a diff.
