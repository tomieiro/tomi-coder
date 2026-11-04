---
name: tomi-coder-prepare
description: Prepare a project or feature in the Tomi style by reading existing structure, choosing tools, and writing tests before implementation. Use to start apps, scripts, modules, or TDD changes.
---

# Tomi Coder Prepare

Read [BASE](references/BASE.md). Deliver a prepared slice with behavioral RED and the minimum structure needed for development. Always use TDD. For a new module, consult the [contract, test, and stub example](references/tdd-example.md).

## Understand before structuring

Find the repository root, local instructions, AICP if present, Git status, relevant README, manifests, locks, tests, and CI. Preserve local changes and verify architecture claims in source. In an empty project, derive the first slice from the request; in an existing one, find its owner and consumers.

Define observable behavior, state, and input/output boundaries. Ask only what blocks that definition; decide reversible details from evidence and record assumptions. Do not create a generic folder tree before understanding the feature.

## Choose tools automatically

Read [tool selection](references/builders.md) when choosing or repairing the environment, runner, or build. Keep what already works. Distinguish environment management, dependency management, task execution, and compilation. Check executables, versions, manifests, and commands. A tool named in a README may not exist locally. Do not invent commands for `riema` or another unidentified tool.

## Prepare with TDD

1. Run the smallest relevant existing checks, if any, and distinguish preexisting failures.
2. Write the first slice's test before functional source: success and contract-relevant errors. Use the existing runner or a minimal appropriate mechanism.
3. Add only the bootstrap required to execute it. After writing the test, add logic-free stubs or signatures if needed. Create directories only for an actual test, domain, entry point, resource, or generated output.
4. Run the test and confirm behavioral RED as defined in BASE. An environment failure does not count.
5. Declare test/build commands and dependencies through the selected mechanism. Generate wrappers and locks with their tools; do not invent versions or hashes. If the environment blocks RED, report preparation as blocked.

Do not implement functional logic in this stage to make tests pass. Prepare one verifiable slice at a time. Tests must express the contract, not an internal solution or artificially narrow sample.

## Handoff

Record the BASE handoff: contract, responsibilities, files, tool choice and evidence, real commands, observed RED, and limits. If only preparation was requested, report intentionally red tests. If development or construction is also requested, continue without routine confirmation.
