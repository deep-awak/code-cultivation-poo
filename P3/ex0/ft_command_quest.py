#!/usr/bin/env python3


import sys


def main() -> None:
    argv = sys.argv
    prog = argv[0]
    args = argv[1:]

    print(f"Program name: {prog}")

    if not args:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(args)}")
        for i, arg in enumerate(args, start=1):
            print(f"Argument {i}: {arg}")

    print(f"Total arguments: {len(argv)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    main()
