#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    test_temperature_input: list[str] = ["25", "abc"]
    for temp_str in test_temperature_input:
        print(f"Input data is '{temp_str}'")
        try:
            temp: int = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
            print("")
        except (ValueError, TypeError) as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
