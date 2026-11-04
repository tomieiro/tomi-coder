# How BASE was inferred

This analysis was performed on 2026-11-03 using six example Git repositories previously supplied under `examples`. Current files, histories of available refs, selected commit statistics, and implementation diffs were inspected. The original projects were neither modified nor run. Adapted excerpts were later anonymized and tested inside the skills; the clones were removed at the user's request. See the [extraction record](code-provenance.md).

## Method and limits

The initial query was `git log --all --no-merges --reverse --author=tomieiro -i`, compared with general logs and commit authors. The histories contain Matheus Tomieiro, MatheusTomieiro, matheustomieiro, and tomieiro aliases. Merge commits were not treated as authorship of integrated work.

All six local clones reported that they were not shallow. This does not prove that every historical branch or unpublished change was available. The analysis is qualitative, not a line-by-line census or proof of the author's thought process. Commits from 2019–2023 were prioritized for the original evolution; the 2026 edits to `lesc-evolution` and `std-moon` were considered a later phase whose use of tools cannot be determined from Git authorship. Several projects were collaborative.

Paths below are relative to each project at the specified commit. The original inspection can be repeated after retrieving the corresponding repositories:

```sh
git -C examples/InternetRelayChat show 8bbe39f -- src/lista_clientes.h src/lista_clientes.c src/servidor.c
git -C examples/InternetRelayChat show b840161 -- src/servidor.c
git -C examples/std-moon show 388bb9e -- fila.lua
```

## Evidence and interpretation

| Project and commits | Observed change | BASE interpretation | Limit |
| --- | --- | --- | --- |
| `std-moon`: `13e150a` → `388bb9e` → `296c189` (2020) | Empty structure files appear first, followed by a stateful queue, then a stack, vector, and documentation. | Name domain pieces and fill them in slices. | Empty files are not a requirement; create only what the current slice needs. |
| `std-moon`: `34ac43d` (2020) | List copying calls a new recursive helper; the `lista.lua` diff shows the integration. | Change the responsible operation when copy behavior changes. | This commit does not prove every copying case is correct; the adaptation documents its limits. |
| `std-moon`: `29d1155` (2022), `4ffac4e` (2026) | Structures move into `DataStructures`, algorithms into `Algorithms`; later folder names become lowercase. | Organization can mature after responsibilities are known. | A rename is not required everywhere, and a 2026 change does not establish the original manual process. |
| `lesc-evolution`: `2124a5a` → `93d5bab` (2020) | Evolution, GUI, and entry point are separated; Make builds parts; constants and the map are explicit in `const/macros.h`. | Separate real responsibilities and show important parameters. | Do not impose C++, macros, headers, or this folder layout on other languages. |
| `lesc-evolution`: `293c12f` (2020) | A diff replaces `std::vector` with allocated arrays and updates access, step count, and cleanup in `main`. | A representation change must follow through its usage and lifecycle. | The commit title suggests the opposite of the diff; do not infer safety gains or recommend manual allocation. |
| `lesc-evolution`: `b23f428`, `8f7e2e9`, `b5af886` | Statistics show localized revisions and a later build cleanup that removed tracked binaries. | Work evolves through revisions; artifacts and builds need explicit review. | Titles and statistics do not prove the corrections' quality. |
| `InternetRelayChat`: `d4f7115`, `5089c7d` (2020) | A small draft is followed by a broad C++ to C change with client, server, and list modules. | Historical architecture is not fixed; boundaries follow the problem. | A historical rewrite does not authorize rewriting current projects. |
| `InternetRelayChat`: `0c17b13` → `89f0dbe` (2020) | Channel/client list changes are followed by server and GUI integration. | A capability reaches its affected modules and needs end-to-end review. | A commit title saying "tested" does not prove automated tests or TDD. |
| `InternetRelayChat`: `8bbe39f` → `b840161` (2020) | Mute/unmute add client state, lookup, and server calls; later a missing-client guard appears. | Build concrete operations and revise error cases. | BASE requires a regression before correction; do not reproduce the unsafe dereference. |
| `AdoPet`: `a8862ea` → `cd26f55` (2019) | Screen controllers start as drafts; the available-items screen later connects data to display and updates a signature and callers. The tree distinguishes `backend`, `bd`, and `frontend`. | Establish integration points, finish a screen at a time, update callers. | Collaborative project: do not attribute the entire architecture to one person or copy static coupling. |
| `AdoPet`: `f2cbb2e`, `581a12b` (2019) | Later corrections focus on `BDConexaoClass.java` after commits described as final. | A completion marker can be provisional; review and repair continue. | Commit scope alone does not prove the database fix works. |
| `lua_notebook`: `b505925` → `66580be` → `b59813b` → `0c73e6e` (2021) | `notebook.lua` starts by consuming `runtime.lua`; the UI and callback then connect input, execution, and output, followed by resource cleanup changes. | Two files can be enough: coordination and operation. Connect results early and review resource lifecycles. | A commit mentioning assertions contains a TODO, not proof of tests; dynamic loading is unsafe for untrusted input. |
| `LicensePicker`: `a38c26d` → `7268059` → `ff0ff9e` → `4226206` (2023) | Android work starts with Activity coordination and resources in assets/layouts, then removes a sample test and changes ignored files and wrapper JAR tracking. | Use native platform structure and concrete operations without invented layers. | Short history; application licensing is unclear, and configured Gradle does not prove a complete executable wrapper. |

## What the sequence shows

A recurring shape is **name the pieces → implement operations → connect behavior → fix observed cases → reorganize when needed**. Some changes are broad, and some examples mix coordination and rules. The operational interpretation is reasoning by domain, data, and operations with freedom to start small. BASE does not copy historical accidents such as tracked binaries, memory risks, shared global state, credentials, incomplete dependencies, or inconsistent names.

The history cannot establish systematic TDD, who wrote every current test, whether commit order matches writing order, whether current versions are entirely manual, or whether every project should use the same language, GUI, Makefile, or folders. Errors are not a required part of human-looking code.

## How the three skills use this

`prepare` retains decomposition into concrete pieces while placing contracts and tests before behavior. `develop` retains direct, incremental implementation while applying Ponytail economy to existing code. `construct` makes later review, correction, build, and artifact checks explicit. Later polish may wait, but a concrete known failure should be tested and corrected when found.

## Provenance and licensing

BASE is an original synthesis. Later code references are identified adaptations with preserved MIT notices. AdoPet, InternetRelayChat, lesc-evolution, lua_notebook, and std-moon have local MIT notices. LicensePicker's former root license was moved into an asset; license texts in assets do not automatically license the app. It was used for observation only. The Ponytail adaptation carries its original MIT notice. The tomi-coder repository retains Apache-2.0.
