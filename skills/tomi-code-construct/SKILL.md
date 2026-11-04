---
name: tomi-code-construct
description: Build, test, and review implementations against the Tomi BASE. Use after development or to inspect changes, compile or package a project, find defects, and correct vulnerabilities through TDD.
---

# Tomi Code Construct

Read [BASE](references/BASE.md). Build and compare the implementation, tests, and artifacts to the contract. Deepen correctness and security review while preserving useful domain boundaries. For a local fix, consult the [before-and-after review example](references/review-example.md), which identifies the historical defect explicitly.

## Recover and review

Read local instructions and architecture context, Git status, and any handoff. Compare the diff with relevant full files, consumers, and tests, including untracked additions. Check TDD evidence. If absent, state the gap; a test run now cannot prove that earlier development used TDD.

Confirm requested behavior and apply the BASE review criteria. File size alone is not a defect. Look for mixed responsibilities, unowned state, duplicated rules, and abstractions with no concrete purpose.

## Find and correct defects

Trace changed paths and boundaries. Depending on the project, examine invalid input, nulls, bounds, error contracts, resource ownership, concurrency, cancellation, authorization, data isolation, secrets, queries, shell execution, paths, serialization, partial writes, transactions, migrations, dependencies, and compatibility.

For each real finding, record its location, trigger, impact, and evidence. Distinguish confirmed issues from suspicions. Rank a concrete integrity, security, or central contract failure as blocking; a secondary failure as relevant; style-only improvements as optional. A scanner does not prove the absence of vulnerabilities.

Correct findings within the authorized scope. For behavioral changes, add a failing regression, observe RED, correct, and confirm GREEN. For structural changes, characterize behavior before and after. Repeat as needed without weakening tests. If the request is review only, report findings and proposed fixes without editing. If a correction needs a conflicting product decision or unavailable access, record the blocker and continue independent checks.

## Build and verify

1. Read recipes and scripts before running them. Use the project's real toolchain; derive missing commands from evidence rather than guessing targets.
2. Run affected and relevant regression tests, static checks, and required project gates. Use applicable scanners already available and report their coverage and limits.
3. Produce the requested local artifact with the actual build or packaging tool. Change generation sources rather than hand-editing generated output. Keep build separate from execution, installation, and publishing.
4. Inspect the produced artifact's path and format and run an appropriate isolated smoke check. For interpreted scripts, use execution or import checks rather than inventing compilation. Report unavailable GUI, device, or service checks.
5. After corrections, rerun affected checks and rebuild invalidated artifacts. Review the final diff and update documentation and architecture context for changed contracts or commands.

Avoid broad cleanup or real services and data for convenience. Do not deploy, publish, commit, or push without explicit authorization.

## Handoff

Report behavior and artifact, BASE alignment, corrections, commands and results, remaining findings, and limits. Mark completion only for the verified scope when relevant checks pass, the artifact is inspected, and no known blocking issue remains. Otherwise report partial or blocked status. Compilation alone does not establish functional correctness or security.
