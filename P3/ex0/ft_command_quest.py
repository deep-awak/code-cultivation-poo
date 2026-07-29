import sys


def main() -> None:
    argv = sys.argv
    print(f"Program name: {argv[0]}")
    if (len(argv) < 2):
        print("No arguments provided!")
    else:
        print(f"Program name: {len(argv) - 1 }")
        for index in range(1, len(argv)):
            print(f"Argument {index}: {argv[index]}")
    print(f"Total arguments: {len(argv)}")


if __name__ == '__main__':
    print("=== Command Quest ===")
    main()
