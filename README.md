# One Word, One Username, One Reward

[![Bounty](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Entry for the make.fun bounty "One Word, One Username, One Reward"
($5, top 3). The entry is the account's own make.fun username, one word
and nothing else.

## Entry

`gaga-kushina`

That is the username of the @gaga-kushina account on make.fun. It is 12
characters, inside the 1 to 30 limit, with no spaces and no extra text.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

`main.py` writes `entry.txt` into `MAKEFUN_OUTPUT_DIR` (default
`/output`). It uses only the Python standard library and makes no network
calls.

## How it works

`main.py` checks the username first: 1 to 30 characters, a single word,
no whitespace. Then it writes the username as UTF-8 with no trailing
newline, sets the file mode to `0644` so the grader can read it, and
reads the file back to confirm the bytes and mode match before exiting.
Every run writes the same bytes.

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
