#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
       int("abc") 
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open("/non/existent/file.txt", "r")
    elif operation_number == 3:
        "str" + 5
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    operation_numbers: list[int] = [0, 1, 2, 3, 4]
    for i in operation_numbers:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        else:
            print("Operation completed successfully\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()