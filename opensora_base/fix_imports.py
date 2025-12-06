#!/usr/bin/env python3
"""
Bulk-rewrite imports from `opensora...` to `opensora...`.

- Replaces:
    opensora.XXX  -> opensora.XXX
    opensora      -> opensora
- Only operates on .py files under the current directory.
- Prints each file it modifies.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent

def fix_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new_text = text

    # First replace the dotted form to preserve attribute chains
    new_text = new_text.replace("opensora.", "opensora.")
    # Then replace any remaining bare `opensora`
    new_text = new_text.replace("opensora", "opensora")

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        print(f"Updated: {path}")
        return True
    return False

def main():
    py_files = list(ROOT.rglob("*.py"))
    print(f"Scanning {len(py_files)} Python files under {ROOT}...")
    changed = 0
    for f in py_files:
        if fix_file(f):
            changed += 1
    print(f"Done. Modified {changed} files.")

if __name__ == "__main__":
    main()

