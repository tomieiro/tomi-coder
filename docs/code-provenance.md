# Code provenance and extraction record

The adapted examples were extracted from local Git repositories on 2026-11-03, before their authorized deletion. The records below identify the exact source revisions and Git blob objects; source clones are not runtime or test dependencies.

Identifiers and domain names inside the snippets are neutralized. Project names, source paths and copyright notices remain in provenance records so anonymization does not erase attribution. The examples are derivatives under the source MIT notices, not a claim of wholly original code.

## Source records

### std-moon: Fila:new and push; state and prepare examples

- Source: [fila.lua at 388bb9e](https://github.com/tomieiro/std-moon/blob/388bb9ed068ceadbb31ecc6629c456709b17b660/fila.lua)
- Commit: `388bb9ed068ceadbb31ecc6629c456709b17b660`
- Source blob: `2c9813e8d7011ab0b5c802db828587e94db524de`
- MIT license blob at that revision: `27b302a0efa7e7b89445cb57d8a04cc83800d48b`

### std-moon: Vetor:at; state and prepare examples

- Source: [vetor.lua at 296c189](https://github.com/tomieiro/std-moon/blob/296c189bad53382141a804355b87d68491749a81/vetor.lua)
- Commit: `296c189bad53382141a804355b87d68491749a81`
- Source blob: `75286abbe84592ff74a3905b1af70652f41629ef`
- MIT license blob at that revision: `27b302a0efa7e7b89445cb57d8a04cc83800d48b`

### std-moon: deep_copy and its call inside Lista:copy; reuse example

- Source: [lista.lua at 34ac43d](https://github.com/tomieiro/std-moon/blob/34ac43def50ca3b9a6e39a1ab9142d2dbaa92f64/lista.lua)
- Commit: `34ac43def50ca3b9a6e39a1ab9142d2dbaa92f64`
- Source blob: `16e02cb31a1055675568bf13ec9ce2e201795d5e`
- MIT license blob at that revision: `27b302a0efa7e7b89445cb57d8a04cc83800d48b`

### InternetRelayChat: lista_buscar_cliente; search and review examples

- Source: [src/lista_clientes.c at 8bbe39f](https://github.com/tomieiro/InternetRelayChat/blob/8bbe39f204454e7b7065c0f22f29a37cbed93aa4/src/lista_clientes.c)
- Commit: `8bbe39f204454e7b7065c0f22f29a37cbed93aa4`
- Source blob: `c543b65d6bd60ed50d647238dd7edfc88299c6c0`
- MIT license blob at that revision: `27b302a0efa7e7b89445cb57d8a04cc83800d48b`

### InternetRelayChat: mute lookup/guard/update; search example

- Source: [src/servidor.c at b840161](https://github.com/tomieiro/InternetRelayChat/blob/b84016107868cb2575a01cb25176804d669b6f8a/src/servidor.c)
- Commit: `b84016107868cb2575a01cb25176804d669b6f8a`
- Source blob: `26ed07b6f541498c221facf92435499ed032b3df`
- MIT license blob at that revision: `27b302a0efa7e7b89445cb57d8a04cc83800d48b`

### lesc-evolution: new_movement and append/count update in Transa; value construction example

- Source: [src/evolution/base.cpp at 293c12f](https://github.com/tomieiro/lesc-evolution/blob/293c12f5ae80f5ac8c80f0b5a2c7bf384d825ba1/src/evolution/base.cpp)
- Commit: `293c12f5ae80f5ac8c80f0b5a2c7bf384d825ba1`
- Source blob: `197134890e6912bb28ecf014e7740cf04a713463`
- MIT license blob at that revision: `27b302a0efa7e7b89445cb57d8a04cc83800d48b`

### lua_notebook: run_code result handling; callback example

- Source: [runtime.lua at 0c73e6e](https://github.com/tomieiro/lua_notebook/blob/0c73e6e9ca5c3c30e48fa61c4fe9420d00ab2130/runtime.lua)
- Commit: `0c73e6e9ca5c3c30e48fa61c4fe9420d00ab2130`
- Source blob: `b9312dea00ca7c5184109ae44c1df763f27d2f89`
- MIT license blob at that revision: `53623c9b98b8a7acce807b494c9a477bb195e1ef`

### lua_notebook: RunCallback result/presentation branch; callback example

- Source: [notebook.lua at b59813b](https://github.com/tomieiro/lua_notebook/blob/b59813baef5656f825915acfdbd26af43117d0ce/notebook.lua)
- Commit: `b59813baef5656f825915acfdbd26af43117d0ce`
- Source blob: `c2590521f8a505078d4d6ae3e95d83e58e0e14fd`
- MIT license blob at that revision: `53623c9b98b8a7acce807b494c9a477bb195e1ef`

### AdoPet: abaDisponiveis; delegation example

- Source: [src/frontend/ChatManager.java at a8862ea](https://github.com/tomieiro/AdoPet/blob/a8862eac5a3f9c272c250a3f3bb5834829240fb8/src/frontend/ChatManager.java)
- Commit: `a8862eac5a3f9c272c250a3f3bb5834829240fb8`
- Source blob: `b5f0ffdda0d19d340fa56865cde9c07d00bb371a`
- MIT license blob at that revision: `d9b6570b2294bd73b24703f75c0ba3f4d15566a0`

## Attribution checks

- Git show and blame attribute the selected queue/vector methods, recursive helper, lookup, mute correction, callback and navigation method to Tomieiro aliases. This establishes repository attribution, not independent authorship of every underlying idea.
- The surrounding std-moon list constructor, append, index and reverse were attributed to Mateus Prado. They were excluded from the personal-style examples; the copy integration retains only Tomieiro's helper and call change, with a new neutral wrapper.
- The surrounding LESC direction/count selection was attributed to Victor Reis. It was excluded. The retained construction helper and sequence write/count update have Tomieiro attribution.
- AdoPet is collaborative. Its selected handler has Tomieiro commit attribution, while its original MIT copyright names Mateus Prado; the original notice is preserved.
- LicensePicker remains architectural evidence only. No source snippet was reused because the app's licensing could not be established from license texts stored as assets.

## Adaptations and coverage

| Example | Preserved behavior | Explicit change |
| --- | --- | --- |
| Prepare/state | Prototype-style object, append, counters, bounds-checked indexed access | Compose selected queue/vector operations; instance-owned state; new TDD tests and stub. |
| Reuse | Recursive key/value/metatable copying and a public operation calling the helper | Neutral module wrapper; no unrelated contributor methods. Cycles and shared identity remain outside the contract. |
| Search/update | Walk, compare, return, guard absence, update one field | Guard null container before access; remove transport parsing; explicit success result. |
| Value construction | Fill a value, write it at the current position, increment count | Local temporary, explicit fixed capacity and capacity guard. |
| Callback | Call operation, normalize nil result, choose presentation based on result type | Trusted callable and output adapter; omit dynamic loading, file capture and GUI styling. |
| Navigation | Handler delegates to existing coordinator | Neutral names; omit framework annotation and unused event argument. |
| Review | Same lookup traversal and match semantics | New regression and an early null guard; defective ordering shown only as historical context. |

## Validation and deletion boundary

Seven executable example checks were first exercised against incomplete stubs, then passed against the adapted snippets in Lua, C, C++ and Java. These are new checks of the adaptations, not historical test evidence. The prepare reference also includes an intentionally failing stub for readers to use in their own TDD cycle.

The package retains the adapted snippets, original MIT notices, commit/blob identifiers and the earlier style report. Full project histories and unrelated source files are not archived in the skills. Before removal, all six example repositories were checked for local changes; deletion is limited to the repository-root examples directory.

The original repository URLs are provenance pointers, not a guarantee of future remote availability. The recorded Git blob identifiers allow a future recovered source to be compared to the inspected version.
