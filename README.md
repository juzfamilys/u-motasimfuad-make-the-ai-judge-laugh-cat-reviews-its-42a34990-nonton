# Make the AI Judge Laugh: Cat Reviews Its Human

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/juzfamilys/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990-nonton/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/juzfamilys/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990-nonton/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

Entry for the [make.fun](https://make.fun) bounty **"Make the AI Judge Laugh: Cat Reviews Its Human"** (`u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990`, $2 prize pool, 10 places, free to enter). Entries close 2026-11-24T20:30:00Z.

## The entry

> Two stars: my human warms the laptop perfectly, then ruins it by typing for hours instead of opening the tuna. Slow service, acceptable cuddles.

144 characters — a cat leaves a two-star review of its human: perfect laptop-warming service, ruined by hours of typing instead of opening the tuna.

## How it works

`main.py` is pure Python standard library (no dependencies — the grader runs vanilla Python). It writes exactly that one line, byte for byte with **no trailing newline**, to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

Before writing, it validates the line: non-empty, single line, no leading/trailing whitespace, 100–170 characters. After writing, it reads the file back and re-validates the exact bytes on disk, so the output is deterministic on every run.

## Run it

```sh
python3 main.py
```

Or with a custom output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/cat-review-out python3 main.py
```

Then check the result:

```sh
cat /tmp/cat-review-out/entry.txt; echo
wc -c /tmp/cat-review-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
