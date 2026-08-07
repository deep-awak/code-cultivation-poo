#!/usr/bin/env python3

import sys
import typing


def read_file(file_name: str) -> str | None:
    file_stream: typing.IO[str] | None = None
    content: str | None = None

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file_stream = open(file_name, "r")
        content = file_stream.read()
        print("---")
        print(content, end="")
        print("---")
    except Exception as e:
        print(f"[STDERR] Error opening file '{file_name}': {e}",
              file=sys.stderr)
    finally:
        if file_stream is not None:
            file_stream.close()
            print(f"File '{file_name}' closed.")

    return content


def transform(content: str) -> str:
    print("Transform data:")
    print("---")
    lines: list[str] = content.rstrip("\n").split("\n")
    transformed_content: str = "".join(f"{line}#\n" for line in lines)
    print(transformed_content, end="")
    print("---")
    return transformed_content


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]}")
        return

    file_name: str = sys.argv[1]
    content: str | None = read_file(file_name)

    if content is None:
        return

    transformed_content: str = transform(content)

    try:
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()

        new_file_name: str = sys.stdin.readline().rstrip("\r\n").strip()

        if not new_file_name:
            print("Data not saved")
            return

        print(f"Saving data to '{new_file_name}'")
        output_stream: typing.IO[str] | None = None
        try:
            output_stream = open(new_file_name, "w")
            output_stream.write(transformed_content)
            print(f"Data saved in file '{new_file_name}'.")
        except Exception as e:
            print(
                f"[STDERR] Error opening file '{new_file_name}': {e}",
                file=sys.stderr,
            )
            print("Data not saved")
        finally:
            if output_stream is not None:
                output_stream.close()
    except (KeyboardInterrupt, EOFError):
        print("\nData not saved")
        return


if __name__ == "__main__":
    main()
