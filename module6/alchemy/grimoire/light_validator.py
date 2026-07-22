from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    all_ingrdts = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    for item in all_ingrdts:
        if item.lower() in ingredients_lower:
            return f"{ingredients}: VALID"

    return f"{ingredients}: INVALID"
