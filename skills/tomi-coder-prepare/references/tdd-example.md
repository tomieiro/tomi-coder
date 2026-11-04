# Prepare example — a concrete object starts with its contract

Adaptation of Tomieiro's `std-moon` methods: `388bb9e`, `fila.lua`,
`Fila:new`/`push`, and `296c189`, `vetor.lua`, `Vetor:at`.
Copyright (c) 2020 Matheus Tomieiro. Original MIT notice:
[EXAMPLES-LICENSE](EXAMPLES-LICENSE).

The historical shape is an object with a collection, counters and direct
operations. Names below are neutral. The tests and the TDD staging are new;
they do not imply the original implementation was developed test-first.

## First slice

The object appends non-nil values to a dense sequence, reports its size and
returns the value at a valid integer index or raises an error for an out-of-range
index. Two instances must not share state.
This needs one module and one test, not a hierarchy of collection interfaces.

Create `test_group.lua` before the functional module:

<!-- snippet: contract-test -->
```lua
local Group = require("group")
local left, right = Group:new(), Group:new()
left:append("alpha")
left:append("beta")
assert(left.size == 2)
assert(left:at(1) == "alpha")
assert(left:at(2) == "beta")
assert(not pcall(function() left:at(3) end))
assert(right.size == 0)
assert(not pcall(function() right:at(1) end))
```

If module loading initially blocks the assertions, create this minimal
`group.lua` stub **after** the test. This block is intentionally incomplete:

<!-- snippet: red-stub -->
```lua
local Group = {}
function Group:new()
    return setmetatable({size = 0}, {__index = self})
end
function Group:append(item) end
function Group:at(index) return nil end
return Group
```

With Lua available, run `lua test_group.lua` from the directory containing both
files. The size assertion must fail because append is not implemented. A
missing interpreter or module error is not the behavioral RED required here.

## Handoff

- **Responsibility:** the module owns the sequence and its operations.
- **Behavior:** append, size, indexed access and independent instance state.
- **Structure:** `group.lua` and `test_group.lua`; no build system is needed yet.
- **RED:** record the actual assertion failure and execution command.
- **Next step:** implement the three operations, run this test to GREEN, then
  inspect callers before expanding the contract.

The historical constructor relied on default state in the prototype table.
The two-instance assertion makes the isolation requirement explicit before
implementation. It does not require introducing factories or dependency
injection: an instance-owned table is sufficient.
