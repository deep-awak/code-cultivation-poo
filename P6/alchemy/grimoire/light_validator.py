from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    validates: list[str] = light_spell_allowed_ingredients()
    for validate in validates:
        if validate.lower() in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
