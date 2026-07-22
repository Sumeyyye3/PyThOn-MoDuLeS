def light_spell_allowed_ingredients() -> list[str]:
    ingredients = ["earth", "air", "fire", "water"]
    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients

    validate_cntr = validate_ingredients(ingredients)

    if "INVALID" in validate_cntr:
        return f"Spell '{spell_name}' rejected -> {validate_cntr}"

    return f"Spell '{spell_name}' recorded -> {validate_cntr}"
