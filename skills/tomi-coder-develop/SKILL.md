---
name: tomi-coder-develop
description: Implement and change code in the Tomi style using prepared structure and TDD. Use for new features, source and script edits, bug fixes, or refactoring with BASE and minimal Ponytail-inspired changes.
---

# Tomi Coder Develop

Read [BASE](references/BASE.md). For existing code, also read the [Ponytail adaptation](references/ponytail.md). New capabilities follow BASE's concrete decomposition; local edits use the smallest complete change. Consult only relevant [anonymized code examples](references/code-examples.md) for state, reuse, search, value construction, callbacks, or navigation. Preserve the reasoning, not unnecessary types or files.

## Recover the slice

Read local instructions and architecture context, pending changes, and the prepare handoff if available. Open tests, affected files, and consumers. Trace input, data, operation, and output before editing. Verify the current state instead of relying solely on an earlier report.

Without preparation, perform the minimal BASE preparation: contract, tools, test written first, and demonstrated RED. Do not require another skill invocation. A currently green test does not prove RED; determine whether behavior already exists, the test is nondiscriminating, or the work advanced since handoff.

## Implement

1. Pick a verifiable slice. Write and run the test before new behavior. Reproduce a bug before fixing it; characterize preserved behavior before a refactor.
2. Implement within the prepared BASE structure. Keep data and operations with their responsibilities; connect them through the entry point. Add a file only for a concrete responsibility.
3. For existing code, find the cause and callers. Reuse local solutions, the standard library, and installed dependencies. Update affected consumers, fixtures, and exports when a signature changes. Fix a shared cause once when that is the right boundary.
4. Run the slice test to GREEN and the affected regression checks. Investigate failures without weakening assertions. Change the contract only when the request warrants it.
5. Refactor only where it helps a real next change, keeping tests green. Repeat for all authorized slices without rewriting adjacent files for visual uniformity.

Initial code may be direct and lightly polished. Never add deliberate bugs, duplication, or poor names to look human. Correct known contract failures and concrete vulnerabilities when found. Record acceptable limits for deeper review.

## Handoff

Report implemented behavior, affected responsibilities, observed RED → GREEN, regression results, and limits. Update the BASE handoff. A blocked or unverified implementation is not complete. Continue to construction when the request covers the full cycle. Do not commit, push, or publish implicitly.
