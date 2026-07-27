def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    valid_units = ["packets", "grams", "area"]
    if unit not in valid_units:
        print("Unknown unit type")
        return

    name = seed_type.capitalize()
    if unit == "packets":
        print(f"{name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{name} seeds: covers {quantity} square meters")
