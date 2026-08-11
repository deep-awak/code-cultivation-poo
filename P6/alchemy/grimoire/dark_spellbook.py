from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = validate_ingredients(ingredients)
    label: str = ""
    if "INVALID" in result:
        label = "Spell rejected"
    else:
        label = "Spell recorded"
    return f"{label}: {spell_name} ({result})"
