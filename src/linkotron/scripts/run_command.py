from __future__ import annotations

import shlex
import subprocess


def run(command: str, with_console: bool = True, line_limit: int | None = None) -> None:
    command_parts = shlex.split(command)
    process = subprocess.run(command_parts, capture_output=True, text=True)
    print()
    if with_console:
        print("```console")
        print(f"$ {command}")

    output = process.stdout.strip()
    if line_limit:
        output = "".join(output.splitlines(keepends=True)[:line_limit]) + "..."

    output = "\n".join(line.rstrip() for line in output.splitlines())
    print(output)

    if with_console:
        print("```")
    print()
