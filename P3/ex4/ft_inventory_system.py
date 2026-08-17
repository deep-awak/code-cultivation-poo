#!/usr/bin/env python3

import sys


def parse_quantity(name: str, qty_str: str) -> int:
    try:
        return int(qty_str)
    except ValueError as e:
        raise ValueError(f"Quantity error for '{name}': {e}")


def validate_item(arg: str, inventory: dict[str, int]) -> tuple[str, int]:
    if ":" not in arg:
        raise ValueError(f"Error - invalid parameter '{arg}'")

    name, qty_str = arg.split(":", 1)

    if name in inventory:
        raise KeyError(f"Redundant item '{name}' - discarding")

    quantity = parse_quantity(name, qty_str)
    return name, quantity


def process_arguments(arguments: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in arguments:
        try:
            name, quantity = validate_item(arg, inventory)
            inventory[name] = quantity
        except (ValueError, KeyError) as e:
            print(e)
    return inventory


def display_inventory_info(inventory: dict[str, int]) -> None:
    print("Got inventory:", inventory)
    print("Item list:", list(inventory.keys()))


def calculate_total_quantity(inventory: dict[str, int]) -> int:
    total = 0
    for qty in inventory.values():
        total += qty
    return total


def display_percentages(inventory: dict[str, int], total_qty: int) -> None:
    if total_qty == 0:
        return
    for name, qty in inventory.items():
        percentage = (qty / total_qty) * 100
        print(f"Item {name} represents {percentage:.1f}%")


def find_extremes(inventory: dict[str, int]) -> tuple[tuple[str, int],
                                                      tuple[str, int]] | None:
    if not inventory:
        return None

    items = list(inventory.items())
    most_abundant = items[0]
    least_abundant = items[0]

    for name, qty in items[1:]:
        if qty > most_abundant[1]:
            most_abundant = (name, qty)
        if qty < least_abundant[1]:
            least_abundant = (name, qty)

    return most_abundant, least_abundant


def main() -> None:
    print("=== Inventory System Analysis ===")
    try:
        arguments: list[str] = sys.argv[1:]
        inventory = process_arguments(arguments)

        display_inventory_info(inventory)

        total_qty = calculate_total_quantity(inventory)
        item_count = len(inventory)
        print(f"Total quantity of the {item_count} items: {total_qty}")

        display_percentages(inventory, total_qty)

        extremes = find_extremes(inventory)
        if extremes:
            most, least = extremes
            print(f"Item most abundant: {most[0]} with quantity {most[1]}")
            print(f"Item least abundant: {least[0]} with quantity {least[1]}")

        inventory["magic_item"] = 1
        print("Updated inventory:", inventory)

    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        pass


if __name__ == "__main__":
    main()
