# Anonymous code examples — the Tomi shape

Read only the examples relevant to the current change. These are adaptations
of selected source functions, not generic examples invented to resemble them.
Domain names, identifiers and UI details are neutralized. The original
language, direct control flow and relationships between operations remain.
Each section identifies any additional correction or extraction.

Anonymization applies to the code's domain, not legal attribution. These
adaptations retain the original MIT notices in [EXAMPLES-LICENSE](EXAMPLES-LICENSE).
Source revisions and functions are listed below; the repository also records
full commit/blob identifiers in `docs/code-provenance.md`. No source clone is
needed to read or execute these snippets.

Use the decision pattern, then adapt to the target project's conventions.
Do not introduce a linked list, recursion, class or static dispatcher just
because one appears here. Tests in this package were written for the adapted
examples; they are not evidence of historical TDD by the original author.

## 1. Put explicit state and its operations together

Sources: `std-moon`, `388bb9e`, `fila.lua`, `Fila:new`, `push`;
`296c189`, `vetor.lua`, `Vetor:at`. The selected methods' blame records identify
Tomieiro, rather than other contributors to the later list implementation.
Copyright (c) 2020 Matheus Tomieiro.

Preserved: a table-backed object, named counters, append as a short state
transition and a bounds check before indexed access. Adaptations: queue append
and vector access are composed in one neutral example; each instance now
owns its collection and counters, avoiding the historical shared-default table.
Only append and indexed access are included; items must be non-nil and dense,
and callers supply integer indices.

<!-- snippet: state -->
```lua
local Group = {}

function Group:new()
    local state = {items = {}, size = 0, first = 1, last = 1}
    self.__index = self
    setmetatable(state, self)
    return state
end

function Group:append(item)
    table.insert(self.items, self.last, item)
    self.size = self.size + 1
    self.last = self.last + 1
end

function Group:at(index)
    if index > #self.items or index < 1 then
        error("Index outside the collection")
    end
    return self.items[index]
end

return Group
```

**Use this when:** a small entity needs a few concrete operations. Keep the data
and the rules close; a generic collection framework would hide this simple flow.
The isolation correction is a good reason for an early two-instance test.

## 2. Reuse an operation to implement the next one

Source: `std-moon`, `34ac43d`, `lista.lua`, Tomieiro's `deep_copy` addition
and the new call to it inside `Lista:copy`.
Copyright (c) 2020 Matheus Tomieiro.

Preserved: recursively copy keys, values and metatables; route the public copy
operation through that helper. Adaptation: the integration point becomes a small
module accepting a collection explicitly. The surrounding historical list class
was contributed by Mateus Prado; its other methods are not used as Tomieiro
style evidence here.

Contract: finite, acyclic tables with accessible, unprotected metatables;
the helper also accepts scalar values. This historical algorithm does not preserve
shared-reference identity and does not handle cycles. If those enter the actual
contract, write the corresponding tests and change the copy operation first.

<!-- snippet: reuse -->
```lua
local function clone_value(value)
    local result
    if type(value) == "table" then
        result = {}
        for key, item in next, value, nil do
            result[clone_value(key)] = clone_value(item)
        end
        setmetatable(result, clone_value(getmetatable(value)))
    else
        result = value
    end
    return result
end

local operations = {}

function operations.copy(items)
    return clone_value(items)
end

return operations
```

**Use this when:** a public operation naturally depends on a shared helper. Reuse the
operation where its semantics fit; do not build a general utility layer first.

## 3. Search once, then change the selected object's state

Sources: `InternetRelayChat`, `8bbe39f`, `src/lista_clientes.c`,
`lista_buscar_cliente`; `b840161`, `src/servidor.c`, the lookup/guard/update
sequence in `mute`. Copyright (c) 2020 Matheus Tomieiro.

Preserved: walk nodes, compare a key, return the selected node, guard absence,
then update one field. Adaptations: neutral types, a guard before reading a
possibly null container, and explicit success/absence return values. Buffer
parsing, network I/O and authorization are outside this extracted data operation.
It is not a replacement for the original command endpoint. Callers provide a
non-null, terminated key and a valid acyclic chain whose keys are also terminated.

<!-- snippet: search -->
```c
#include <stddef.h>
#include <string.h>

typedef struct Entry {
    const char *key;
    int marked;
    struct Entry *next;
} Entry;
typedef struct { Entry *first; } Catalog;

Entry *find_entry(Catalog *catalog, const char *key) {
    if (catalog == NULL) return NULL;
    Entry *current = catalog->first;
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) return current;
        current = current->next;
    }
    return NULL;
}

int mark_entry(Catalog *catalog, const char *key) {
    Entry *current = find_entry(catalog, key);
    if (current == NULL) return 0;
    current->marked = 1;
    return 1;
}
```

**Use this when:** multiple actions need the same lookup. Keep the lookup and
the caller's state transition visible. Do not duplicate the search in each action.

## 4. Build a value once and reuse it in the state transition

Source: `lesc-evolution`, `293c12f`, `src/evolution/base.cpp`, `new_movement`
and Tomieiro's append/count update inside `Transa`.
Copyright (c) 2020 Matheus Tomieiro.

Preserved: assemble a value in a small helper, put it at the current sequence
position and advance the count. Adaptations: the temporary result is local
instead of global; a four-slot buffer makes ownership visible without allocation;
an explicit capacity guard prevents an out-of-bounds write. The sequence starts
zero-initialized and is modified only through this operation.

The surrounding direction/count selection in that revision was contributed by
Victor Reis according to blame, so it is not presented as Tomieiro's own logic.
Population management, randomness and maze movement are outside this excerpt.

<!-- snippet: decisions -->
```cpp
struct Step { char direction; unsigned char count; };
struct Sequence { Step steps[4]; unsigned int size; };

Step make_step(char direction, unsigned char count) {
    Step result;
    result.direction = direction;
    result.count = count;
    return result;
}

bool append_step(Sequence &sequence, char direction, unsigned char count) {
    if (sequence.size >= 4) return false;
    sequence.steps[sequence.size] = make_step(direction, count);
    sequence.size++;
    return true;
}
```

**Use this when:** one helper constructs a value used by concrete state changes.
Keep the creation, write and counter update readable. The capacity check is an
explicit correction for the adaptation, not a claim about the historical source.

## 5. Keep execution and presentation connected through a small module

Sources: `lua_notebook`, `0c73e6e`, `runtime.lua`, the result-handling branch of
`runtime.run_code`; `b59813b`, `notebook.lua`, `RunCallback`.
Copyright (c) 2021 Matheus Tomieiro.

Preserved: call an operation, normalize a nil return to true, and let the
callback choose how to present the result. The historical callback treats
boolean results as an error display; that oddity is kept visible here, not
silently corrected. Adaptations: a trusted callable replaces parsing/loading
source text; output capture and GUI styling are omitted; `output:set` is the
small presentation boundary supplied by the caller. Exceptions propagate.
This demonstrates composition, not a sandbox for untrusted code.

<!-- snippet: callback -->
```lua
local processor = {}

function processor.run(action)
    if action == nil then return nil end
    local result = action()
    if result == nil then return true end
    return result
end

function processor.on_action(action, output)
    local response = processor.run(action)
    if not (type(response) == "nil" or type(response) == "boolean") then
        output:set(response)
    else
        output:set("error")
    end
end

return processor
```

**Use this when:** a UI or command callback coordinates a small operation.
Test the operation and the presentation decision separately. If a new product
needs successful no-result actions to display success, change that contract
with a test; do not mistake a historical convention for a universal rule.

## 6. Let a screen action delegate to the existing navigation point

Source: `AdoPet`, `a8862ea`, `src/frontend/ChatManager.java`, `abaDisponiveis`.
The selected method was introduced in a Tomieiro commit; the project is
collaborative. Its MIT notice is Copyright (c) 2019 Mateus Prado.

Preserved: the handler delegates directly to the screen coordinator. Adaptation:
neutral names, removal of framework annotation and unused event parameter.
`Screens` is the existing application's coordinator; the snippet does not
introduce a navigation framework. The test supplies a minimal stand-in.

<!-- snippet: delegation -->
```java
class PanelActions {
    void openList() {
        Screens.showList();
    }
}
```

**Use this when:** the application already has a navigation entry point. A thin
handler is enough. Keep domain rules out of the handler as the feature grows.

## What to carry into new code

- State and operations have a concrete owner.
- Reuse follows a real dependency between operations.
- Branches express the actual decision instead of hiding it in machinery.
- Callbacks connect existing pieces without taking over all their work.
- Local corrections improve the contract while preserving understandable flow.

The examples are not a template to paste wholesale. Preserve their reasoning,
the requested TDD cycle and the receiving project's contracts.
