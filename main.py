#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes this account's own make.fun username, and nothing else, to
``entry.txt`` inside the output directory.

The entry is the single word ``gaga-kushina``: the username of the
@gaga-kushina account on make.fun. No explanation, no links, no pitch.
"""

import os
import stat
import sys

USERNAME = "gaga-kushina"


def validate(username: str) -> str | None:
    """Return an error message when the entry breaks the gate, else None."""
    if not username:
        return "username is empty"
    if len(username) > 30:
        return f"username is {len(username)} characters, over the 30 limit"
    if username != username.strip() or any(ch.isspace() for ch in username):
        return "username must be a single word with no spaces"
    return None


def main() -> int:
    # The gate accepts UTF-8 text of 1 to 30 characters, not only
    # whitespace, so check the entry before anything is written.
    error = validate(USERNAME)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    data = USERNAME.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    # The grader collects outputs as another user, so the file has to
    # be readable by everyone.
    os.chmod(path, 0o644)

    # Read the file back and confirm it holds exactly the entry.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != data:
        print("entry.txt does not match the username", file=sys.stderr)
        return 1
    if stat.S_IMODE(os.stat(path).st_mode) != 0o644:
        print("entry.txt is not mode 0644", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
