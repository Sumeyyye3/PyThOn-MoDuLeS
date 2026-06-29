import alchemy


def main() -> None:
    print("\n\n\n=== Distillation 1 ===\n")
    print("Using: 'import alchemy' structure to access potions")
    print("Creating is strength_position ", end="")
    print(alchemy.strength_potion())
    print("Creating is heal alias (healing_potions) ", end="")
    print(alchemy.heal())


main()
