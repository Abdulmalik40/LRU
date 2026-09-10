## How this repo is laid out

- `main.py` — the program you're grading right now.
- `tests/` — the public test cases per lesson (`tests/01-…/1.in` → expected `1.out`).
- `run_tests.sh` — the local runner. `.shipthatcode.json` tells the grader what this repo is; don't delete either.

### One lesson at a time

Each lesson states its own input and output format, and **most lessons are a separate exercise rather than a bigger version of the last one**. Two lessons can be handed the same input line and correctly want different output — a tokenizer prints `[ls] [-la]`, while the next lesson, which receives already-tokenized input, prints `ls -la`. No single program can satisfy both, and it isn't supposed to.

So treat `main.py` as the file for the lesson you're grading: when you move on, change what it does. Nothing is lost — every earlier lesson is in your git history (`git log`, `git show`), and shipthatcode remembers each lesson you passed, so a lesson stays completed even after you replace the code that passed it. If you'd rather keep the code visible, copy it aside first (`cp main.py solutions/01-<lesson>.py`) — extra files are ignored by the grader.

When a lesson genuinely does build on the previous one, its own text says so and its tests will pass with the earlier behaviour still in place.

