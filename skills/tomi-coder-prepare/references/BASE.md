# BASE — developing the Tomi way

This is the shared reference for `tomi-coder-prepare`, `tomi-coder-develop`, and `tomi-code-construct`. Read it before working. The style was inferred from files and commit diffs in six example projects supplied earlier. It is an operational interpretation, not an infallible account of the author. The repository report `docs/style-and-evidence.md` records the observations; the provenance record `docs/code-provenance.md` identifies the adapted code. Each skill carries its own copy of this reference and works without the original clones.

## Requirements and evidence

- **Current request:** always use TDD; prepare, develop, then construct and review; use this BASE for new capabilities and Ponytail-inspired restraint for local changes.
- **Historical inference:** identify concrete parts, implement direct operations, connect the flow, and revise it as behavior becomes observable.
- **Limit:** commit authorship does not prove exclusive authorship of a file or systematic TDD. Collaborative projects and later edits do not define an immutable personal style.

## Shape the code around the problem

1. **Start with observable behavior.** Identify inputs, state changes, and outputs. Name parts after domain concepts such as channel, client, population, screen, or report. Do not start with a catalog of architectural layers.
2. **Give each real responsibility a home.** A module may hold an entity and its operations; another coordinates interaction. A small script can remain one file. One responsibility does not automatically need a service, interface, and implementation.
3. **Make state traceable.** Show which fields, arguments, and collections change, and who owns resources. This does not mandate globals, pointers, or classes.
4. **Write concrete operations.** Use domain verbs and direct control flow. Prefer idiomatic language features over generic machinery that obscures a short sequence.
5. **Connect a usable slice.** Follow input → operation → output. A GUI, CLI, route, or `main` coordinates the flow; extract only the rule that needs testing without a live window, network, or database.
6. **Advance from observed needs.** Finish one slice, run it, correct it, then continue. Intermediate work may be incomplete if its status and limits are explicit.
7. **Change representations for a concrete reason.** When a collection, signature, or file boundary changes, protect the contract with tests and update affected consumers. A small feature does not justify a repository-wide redesign.
8. **Keep important parameters visible.** Use named constants or existing configuration for values that require understanding or tuning. Do not invent a configuration system for hypothetical needs.
9. **Write for the next maintainer.** Follow the target project's language and conventions. Use domain names and comments about intent, limits, and contracts. Do not imitate typos, slang, redundant comments, or vague commit titles.

The first implementation can be direct and imperfectly polished. Never introduce defects intentionally. Turn discovered failures into tests and corrections, and state known limits. Validate external inputs, protect data, and enforce required access controls in the first applicable slice.

## New capability or existing code

| Situation | Decision |
| --- | --- |
| New app or capability | Define behavior and a test first; create the concrete parts needed for its first slice. |
| New file in an existing feature | Choose its owner from the domain and local structure; a new file need not create a new architecture. |
| Local fix or extension | Trace callers and effects; make the smallest complete change within the existing structure. |
| Refactor | Characterize preserved behavior first; justify each structural change. |
| Tiny new project | Use only files and tools needed for the first verifiable behavior. |
| Established architecture | Work within its existing boundaries; do not impose another project's historical layout. |

BASE guides how capabilities grow. The Ponytail adaptation guides economy of change without removing a requested feature, a useful boundary, or a required test. Minimize the **complete** change, not the character count.

## Always TDD

For every new, changed, or corrected behavior:

1. **Contract:** describe a situation, action, and observable result. Include error cases belonging to this slice. Do not encode an invented internal design in the test.
2. **RED:** write and run the test before functional implementation. Confirm that it fails for the expected missing behavior. A broken environment, unavailable dependency, or undiscovered test is not RED.
3. **GREEN:** implement the contract, not merely one sample. Run that test and affected regression checks.
4. **REFACTOR:** improve only what has a concrete reason while keeping tests green and the domain flow readable.

Never implement behavior before its test. Do not weaken assertions, skip tests, or change expectations solely to obtain GREEN. Record genuine contract changes.

**Bootstrap:** create the minimum test runner, manifest, directory, or signature needed to run the test. Create the test file before functional source. If an absent import prevents an assertion, add only a logic-free stub to reach a behavioral failure. Do not launch a full app to test a small rule.

**Legacy code:** characterize behavior that must remain. Add a failing regression before fixing a defect. A behavior-preserving refactor may start with green characterization tests; do not invent a defect to manufacture RED.

**Structure, build, and configuration:** when a change alters executable behavior, write the relevant contract, integration, or smoke check first. For documentation-only changes, inspect references and consistency rather than inventing a text-matching test.

**Blocked environment:** record the command and obstacle. Continue independent inspection and preparation, but do not claim RED or GREEN or implement behavior whose cycle cannot be observed.

## Handoff between stages

Use an existing task record. If work must resume in another session and none exists, create one `TOMI-TASK.md` at the root without overwriting another task. A short continuous task may use a handoff message. Carry forward:

```text
Objective and observable contract:
Current slice and module responsibilities:
Affected test and implementation files:
Selected tools and evidence for the choice:
Commands (directory, environment, test, regression, build, smoke):
RED: command, test, observed failure, code state:
GREEN: command, observed result, code state, or not yet run:
Deliberate limits, risks, and blockers:
Next stage and outstanding work:
```

Commands must be real and verified for the project. Explain inapplicable fields briefly. Record observed results, not predictions. Refer to an existing commit or describe files and diffs; do not create commits automatically. Later changes invalidate affected evidence.

- **prepare → develop:** minimal structure, demonstrated RED, defined commands and contracts. RED is an expected preparation result.
- **develop → construct:** implemented slice with affected tests GREEN; state limits and pending review. Do not claim the project is distribution-ready before verification.
- **construct → completion:** review against BASE, regression, build or equivalent, and artifact smoke check; report what passed, failed, or was blocked.

If invoked alone, a stage reconstructs missing prerequisites within the authorized scope. Do not require the user to invoke another skill. For a request covering the whole cycle, continue between stages automatically.

## Operational boundaries

Read local instructions and architecture context before editing, and verify claims against real files. Preserve user changes. BASE does not authorize publishing, destructive migrations, global installation, or changes to external services. A local build does not imply deployment. Read task recipes before running them; a harmless-looking target may start a service or install packages.

Security and integrity are not postponed polish. Construct performs deeper review, but test and fix a concrete problem as soon as it is found. Cosmetic cleanup and speculative generalization may wait; known data loss, secret exposure, or contract failure may not.

## Review for BASE alignment

Look for evidence without a numerical style score:

- Does each module own a real responsibility with understandable data, operations, and consumers?
- Is the path from input through state change to output clear?
- Does the change preserve contracts and reach affected consumers?
- Was the relevant test written first, and is the observed cycle recorded?
- Does the solution use existing structure and add only justified abstractions?
- Are limits explicit, and can the next adjustment be localized?

Correct a deviation when it harms behavior, modularity, security, or concrete maintenance. A difference in taste alone does not justify a rewrite.
