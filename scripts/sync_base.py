"""Sincronizar a BASE comum nas três skills instaláveis."""

import argparse
from pathlib import Path

SKILLS = ("tomi-coder-prepare", "tomi-coder-develop", "tomi-code-construct")


def sync_base(root, write=False):
    content = (root / "BASE.md").read_bytes()
    changed = []
    for skill in SKILLS:
        target = root / "skills" / skill / "references" / "BASE.md"
        if not target.exists() or target.read_bytes() != content:
            changed.append(target)
            if write:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    return changed


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="atualizar as cópias")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    changed = sync_base(root, write=args.write)
    for path in changed:
        print(f"{'Atualizada' if args.write else 'Divergente/ausente'}: {path.relative_to(root)}")
    if not changed:
        print("BASE sincronizada nas três skills.")
    return 0 if args.write or not changed else 1


if __name__ == "__main__":
    raise SystemExit(main())
