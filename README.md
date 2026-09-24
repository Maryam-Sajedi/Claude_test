
The Fibonacci sequence starts with 0 and 1, and each following number is the sum of the two before it:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

The script has two versions of the same recursive function:

| Mode   | Function   | How it works | Time complexity |
|--------|------------|--------------|-----------------|
| `slow` | `fib_slow` | Plain recursion. It calculates the same values again and again. | O(2ⁿ) |
| `fast` | `fib_fast` | The same recursion, wrapped in `functools.lru_cache`, so each value is computed only once and then reused. | O(n) |

The `timed` helper uses `time.perf_counter()` to measure how long each version takes.

## Requirements

- Python 3.8 or newer
- No extra packages. The script uses only the standard library (`argparse`, `time`, `functools`).

## Usage

```bash
python3 fibonacci.py <n> [--mode {slow,fast,both}]
```

| Argument | Description |
|----------|-------------|
| `n`      | Which Fibonacci number to compute (for example `30`) |
| `--mode` | Which version to run: `slow`, `fast`, or `both` (default: `both`) |

### Examples

Compare both versions:

```bash
python3 fibonacci.py 30
```

```
[slow]  fib(30) = 832040  (took 0.062753s)
[fast]  fib(30) = 832040  (took 0.000024s)
```

Run only the fast version, which can handle much larger numbers:

```bash
python3 fibonacci.py 200 --mode fast
```

Show the help text:

```bash
python3 fibonacci.py --help
```

## Notes

- The slow version gets very slow quickly. Each step up in `n` makes it about 1.6× slower, so values above about 35 can take a long time. Use `--mode fast` for bigger numbers.
- The fast version uses recursion, so very large values of `n` (around 1000 and above) hit Python's recursion limit.
- Timings depend on your machine.

## Other projects in this repo

- [Cookie Monster Weight Predictor](COOKIE_MONSTER.md): predicts Cookie Monster's birthday weight with a Monte Carlo simulation (`cookie_monster.py`).
