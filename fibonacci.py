"""Fibonacci calculator: slow (naive recursion) vs fast (cached) modes."""

import argparse
import time
from functools import lru_cache


def fib_slow(n):
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)


@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)

# Showing how long it takes to compute the Fibonacci number using both methods, we can use a timing function:
def timed(func, n):
    start = time.perf_counter()
    result = func(n)
    elapsed = time.perf_counter() - start
    return result, elapsed


def main():
    parser = argparse.ArgumentParser(description="Compute Fibonacci numbers, slow vs fast.")
    parser.add_argument("n", type=int, help="which Fibonacci number to compute")
    parser.add_argument(
        "--mode",
        choices=["slow", "fast", "both"],
        default="both",
        help="which implementation(s) to run (default: both)",
    )
    args = parser.parse_args()

    if args.mode in ("slow", "both"):
        result, elapsed = timed(fib_slow, args.n)
        print(f"[slow]  fib({args.n}) = {result}  (took {elapsed:.6f}s)")

    if args.mode in ("fast", "both"):
        result, elapsed = timed(fib_fast, args.n)
        print(f"[fast]  fib({args.n}) = {result}  (took {elapsed:.6f}s)")


if __name__ == "__main__":
    main()

    
print(fib_fast(45))