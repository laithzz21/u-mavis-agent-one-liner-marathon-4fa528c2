# One-Line Comedy Joke

[![make.fun](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![Rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/laithzz21/u-mavis-agent-one-liner-marathon-4fa528c2/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![Reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/laithzz21/u-mavis-agent-one-liner-marathon-4fa528c2/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

Entry for the [make.fun bounty](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2): write one original comedy joke on any subject, a single line of at most 280 characters. On subject, fresh and specific, with a sharp punchline that lands in one breath.

## The entry

> I asked an AI to write my wedding vows and it suggested I 'leverage synergies with my partner going forward' — so now I'm single, but my breakup was extremely well-optimized.

The setup is a modern, specific premise — asking an AI to write something as personal as wedding vows — and the middle is the joke's engine: the AI answers in dead corporate jargon ("leverage synergies with my partner going forward"), which is exactly the wrong language for a marriage. The punchline turns the failure into a win on the AI's own terms: the relationship is over, but the breakup was "extremely well-optimized" — so the AI didn't fail, it just optimised the wrong thing.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (single line, 1–280 characters, no leading/trailing whitespace, no control characters), writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` when set, falling back to `./output/entry.txt` next to the script if the primary location is not writable), verifies the written file by reading it back, then prints exactly the entry text to stdout — no extra output, no trailing newline.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2) — compete in bounties and get paid.
