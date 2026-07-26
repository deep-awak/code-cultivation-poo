#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0:
        raise ValueError(f"Caught input_temperature error: {temperature}°C is \
too cold for plants (min 0°C)")
    elif temperature > 40:
        raise ValueError(f"Caught input_temperature error: {temperature}°C is \
too hot for plants (max 40°C)")
    else:
        return temperature


def test_temperature() -> None:
    test_temperature_inputs: list[str] = ["25", "abc", "100", "-50"]
    for temp_str in test_temperature_inputs:
        print(f"Input data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C\n")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
            print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature()
