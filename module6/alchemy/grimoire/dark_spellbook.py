from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients = ["bats", "frogs", "arsenic", "eyeball"]
    return ingredients


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validate_cntr = validate_ingredients(ingredients)
    if "INVALID" in validate_cntr:
        return f"Spell '{spell_name}' rejected -> {validate_cntr}"
    return f"Spell '{spell_name}' recorded -> {validate_cntr}"
