#!/usr/bin/env python3

import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    file_name: str = sys.argv[1]
    file_stream: typing.IO[str] | None = None

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        file_stream = open(file_name, "r")
        content: str = file_stream.read()
        print("---")
        print(content, end="")
        print("---")
    except Exception as e:
        print(f"Error opening file '{file_name}': {e}")
    finally:
        if file_stream is not None:
            file_stream.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
