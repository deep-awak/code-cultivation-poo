#!/usr/bin/env python3

def secure_archive(
    filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                data: str = file.read()
            return (True, data)
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: '{action}'")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    res: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(res)

    if res[0]:
        print("\nUsing 'secure_archive' to write previous\
 content to a new file:")
        print(secure_archive("new_archive.txt", action="write",
                             content=res[1]))


if __name__ == "__main__":
    main()
