import alchemy.transmutation as transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print(f"Testing lead to gold: {transmutation.recipes.lead_to_gold()}")
