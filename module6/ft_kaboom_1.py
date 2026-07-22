def main() -> None:
    print("\n\n\n=== Kaboom 1 ===\n\n")
    print("Using grimoire module directly\n")

    from alchemy.grimoire.dark_spellbook import dark_spell_record

    print(dark_spell_record("Nightmare", "bats and arsenic"))


if __name__ == "__main__":
    main()
