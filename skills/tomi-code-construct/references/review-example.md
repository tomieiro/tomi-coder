# Review example — repair the boundary, preserve the traversal

Adapted from `InternetRelayChat`, `8bbe39f`, `src/lista_clientes.c`,
`lista_buscar_cliente`. Copyright (c) 2020 Matheus Tomieiro; original MIT
notice: [EXAMPLES-LICENSE](EXAMPLES-LICENSE).

The method was introduced in that Tomieiro commit. Names and types below are
neutralized. The defect and the traversal are visible without the original
network server. The fix and regression are new adaptations, not claims that
the original commit already contained them.

## Before: historical ordering defect, not a recommended implementation

This excerpt reads the container before checking it. It is deliberately shown
only to explain the finding; do not execute it with a null container.

```c
Entry *current = catalog->first;
if (catalog != NULL) {
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) return current;
        current = current->next;
    }
}
return NULL;
```

**Finding:** `catalog == NULL` reaches a dereference before the guard, causing
undefined behavior. The correction belongs in the lookup boundary. A guard in
one action would leave other callers exposed. This finding does not require
replacing the linked list or redesigning the command server.

## Write the regression before correcting the source

```c
assert(find_entry(NULL, "alpha") == NULL);
Catalog empty = {NULL};
assert(find_entry(&empty, "alpha") == NULL);
Entry item = {"alpha", NULL};
Catalog full = {&item};
assert(find_entry(&full, "alpha") == &item);
assert(find_entry(&full, "absent") == NULL);
```

The present package tests these cases against the full corrected block below.
In a real repair, run the regression against the old implementation in an
isolated test process, observe its failure, then make the change.

## After: one early guard, same search algorithm

<!-- snippet: fixed-search -->
```c
#include <stddef.h>
#include <string.h>

typedef struct Entry { const char *key; struct Entry *next; } Entry;
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
```

The key must still be non-null and terminated, and nodes must form a valid,
acyclic chain with terminated keys. The guard does not claim to validate memory
ownership, concurrency or every possible pointer. Check those contracts in the
real application when relevant.

## Review conclusion

- **BASE preserved:** explicit data, direct traversal and a reusable lookup.
- **Defect corrected:** the absence check now precedes access to the container.
- **Regression scope:** absent container, empty container, match and no match.
- **Verification:** compile with warnings enabled, run the regression, then
  rebuild affected callers; compilation alone does not exercise the defect.
- **No architectural expansion:** introduce a different collection or ownership
  model only if an observed requirement calls for it.
