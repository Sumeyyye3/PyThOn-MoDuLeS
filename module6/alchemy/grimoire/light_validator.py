from alchemy.grimoire import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    all_ingrdts = light_spell_allowed_ingredients()
    for i in all_ingrdts:
        if ingredients.capitalize() == all_ingrdts[i].capitalize():
            return "VALID"
        i = i + 1
    return "INVALID"
