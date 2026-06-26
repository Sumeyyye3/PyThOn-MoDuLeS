def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:

    new_seed_type = seed_type.capitalize()

    if unit == "packets":
        unit = "packets available"

    elif unit == "grams":
        unit = "grams total"

    elif unit == "area":
        unit = "covers"
        unit_second = "square meters"

    else:
        print("Unknown unit type")
        return

    if unit != "covers":
        print(new_seed_type, "seeds:", quantity, unit)
        return

    print(new_seed_type, "seeds:", unit, quantity, unit_second)
