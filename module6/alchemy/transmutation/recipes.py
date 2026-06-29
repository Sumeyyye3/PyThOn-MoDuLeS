from elements import create_fire
from alchemy.elements import create_air
from alchemy.potions import strength_potion


def lead_to_gold() -> None:
    fire = create_fire()
    air = create_air()
    strength = strength_potion()
    print(f"Recipe transmuting Lead to Gold: brew ’{air}’", end="")
    print(f" and ’{strength}’ mixed with {fire}")
