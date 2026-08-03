#!/usr/bin/env python3


import sys


def parse_scores(args: list[str]) -> list[int]:
    valid: list[int] = []
    for arg in args:
        try:
            valid += [int(arg)]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return valid


def display_stats(scores: list[int]) -> None:
    if not scores:
        print(f"No scores provided. Usage: python3 {sys.argv[0]}\
 <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    total = sum(scores)
    count = len(scores)
    avg = total / count
    high = max(scores)
    low = min(scores)
    range_ = high - low

    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {avg:.1f}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {range_}")


def main() -> None:
    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    if not args:
        print(f"No scores provided. Usage: python3 {sys.argv[0]}\
 <score1> <score2> ...")
        return

    scores = parse_scores(args)
    display_stats(scores)


if __name__ == "__main__":
    main()
