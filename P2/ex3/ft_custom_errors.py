#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_custom_exceptions() -> None:

    print("\nTesting PlantError...")
    days_since_last_watered: int = 4
    try:
        if days_since_last_watered > 2:
            raise PlantError("The tomato plant is wilting!")
        print("The tomato plant is blooming beautifully!")
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    water_tank_stock_liters: float = 2.5
    try:
        if water_tank_stock_liters < 5:
            raise WaterError("Not enough water in the tank!")
        print("There is enough water in the tank!")
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def test_garden_error_exceptions() -> None:
    print("\nTesting catching all garden errors...")
    days_since_last_watered: int = 4
    try:
        if days_since_last_watered > 2:
            raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    water_tank_stock_liters: float = 2.5
    try:
        if water_tank_stock_liters < 5:
            raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught GardenError: {error}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_exceptions()
    test_garden_error_exceptions()
    print("\nAll custom error types work correctly!")
