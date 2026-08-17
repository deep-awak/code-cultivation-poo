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
        print(f"Error opening file '{file_name}': {e}")
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
        print("Usage: ft_archive_creation.py <file>")
        return

    file_name: str = sys.argv[1]
    content: str | None = read_file(file_name)

    if content is None:
        return

    transformed_content: str = transform(content)

    try:
        new_file_name: str = input(
            "Enter the name of the file to save to (leave empty to skip): "
        ).strip()

        if not new_file_name:
            print("No file name provided. Saving skipped.")
            return

        print(f"Saving data to '{new_file_name}'")
        output_stream: typing.IO[str] | None = None
        try:
            output_stream = open(new_file_name, "w")
            output_stream.write(transformed_content)
            print(f"File '{new_file_name}' saved successfully.")
        except Exception as e:
            print(f"Error writing file '{new_file_name}': {e}")
        finally:
            if output_stream is not None:
                output_stream.close()
    except (KeyboardInterrupt, EOFError):
        print("\nOperation cancelled.")
        return


if __name__ == "__main__":
    main()
