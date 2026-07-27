#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name is not None and plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(plants_name: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant_name in plants_name:
            water_plant(plant_name)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    valid_plants: list[str] = ["Tomato", "Lettuce", "Carrots"]
    print("Testing valid plants...")
    test_watering_system(valid_plants)

    invalid_plants: list[str] = ["Tomato", "lettuce", "Carrots"]
    print("\nTesting invalid plants...")
    test_watering_system(invalid_plants)

    print("\nCleanup always happens, even with errors!")
