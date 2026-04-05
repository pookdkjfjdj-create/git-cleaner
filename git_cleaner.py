#!/usr/bin/env python3
"""git-cleaner -- interactive git branch and tag cleanup."""

from __future__ import annotations

import subprocess
import sys


def run(cmd: str | list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True, shell=isinstance(cmd, str)).stdout.strip()


def list_branches(merged: bool = True) -> list[str]:
    flag = "--merged" if merged else ""
    out = run(f"git branch --no-color {flag}")
    return [
        line.strip().lstrip("* ")
        for line in out.splitlines()
        if line.strip() and line.strip().lstrip("* ") not in ("main", "master", "develop")
    ]


def list_tags(preserved: list[str] | None = None) -> list[str]:
    preserved = preserved or []
    out = run("git tag")
    return [t for t in out.splitlines() if t.strip() and t not in preserved]


def dry_run(merged_only: bool = True) -> str:
    branches = list_branches(merged=merged_only)
    tags = list_tags()
    lines = ["Dry-run cleanup report", ""]
    lines.append(f"Branches to delete ({len(branches)}):")
    for b in branches:
        lines.append(f"  {b}")
    lines.append("")
    lines.append(f"Tags to delete ({len(tags)}):")
    for t in tags:
        lines.append(f"  t")
    if not branches and not tags:
        lines.append("Nothing to clean!")
    return "\n".join(lines)


def execute(merged_only: bool = True, dry: bool = False) -> str:
    branches = list_branches(merged=merged_only)
    tags = list_tags()

    actions: list[str] = []
    if dry:
        return dry_run(merged_only)

    for b in branches:
        run(f"git branch -d {b}")
        actions.append(f"Deleted branch: {b}")

    for t in tags:
        run(f"git tag -d {t}")
        actions.append(f"Deleted tag: {t}")

    if not actions:
        return "Nothing to clean!"
    return "\n".join(actions)


def main() -> None:
    if len(sys.argv) < 2 or sys.argv[1] in ('--help', '-h'):
        print('Usage:')
        print('  python -m git_cleaner list')
        print('  python -m git_cleaner list --unmerged')
        print('  python -m git_cleaner delete --dry-run')
        print('  python -m git_cleaner delete')
        return

    cmd = sys.argv[1]
    if cmd == 'list':
        merged = '--unmerged' not in sys.argv
        branches = list_branches(merged=merged)
        tags = list_tags()
        mode = "merged" if merged else "all"
        print(f"Branches ({mode}, {len(branches)}):")
        for b in branches:
            print(f"  {b}")
        print(f"\nTags ({len(tags)}):")
        for t in tags:
            print(f"  {t}")
    elif cmd == 'delete':
        dry = '--dry-run' in sys.argv
        merged = '--unmerged' not in sys.argv and '--all' not in sys.argv
        print(execute(dry=dry, merged_only=merged))
    else:
        print(f'Unknown command: {cmd}')
        sys.exit(1)


if __name__ == '__main__':
    main()
