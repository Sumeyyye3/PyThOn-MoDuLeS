from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("\n\n\n=== Distillation 0 ===\n")
    print("Direct access to alchemy/potions.py")
    print("Healing is creating ", end="")
    print(healing_potion())
    print("Strength is creating ", end="")
    print(strength_potion())
    print("\n\n\n")
