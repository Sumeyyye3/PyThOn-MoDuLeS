from alchemy.grimoire import validate_ingredients


def light_spell_allowed_ingredients() -> list[str, str, str, str]:
    ingredients = ["earth", "air", "fire", "water"]
    return ingredients


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate_cntr = validate_ingredients(ingredients)
    if validate_cntr:
        return "VALIDATE IS OK"
    else:
        return "VALIDATE IS NO	"
