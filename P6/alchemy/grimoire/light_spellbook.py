def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    result: str = validate_ingredients(ingredients)
    label: str = ""
    if "INVALID" in result:
        label = "Spell rejected"
    else:
        label = "Spell recorded"
    return f"{label}: {spell_name} ({result})"
