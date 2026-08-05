from typing import Any


def artifact_sorter(
        artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    power_values = lambda a: a["power"]  # noqa: E731
    sorted_list = sorted(artifacts, key=power_values, reverse=True)
    return sorted_list


def power_filter(
        mages: list[dict[str, Any]],
        min_power: int
) -> list[dict[str, Any]]:
    filtered_list = list(filter(lambda mage:
                                mage["power"] > min_power, mages))
    return filtered_list


def spell_transformer(spells: list[str]) -> list[str]:
    spell_names = list(map((lambda x: "*" + x + "*"), spells))
    return spell_names


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    max_mage = max(mages, key=(lambda x: x["power"]))
    min_mage = min(mages, key=(lambda x: x["power"]))
    powers = list(map((lambda x: x["power"]), mages))
    average = round(sum(powers) / len(mages), 2)
    new_dict = {
        "max_power": max_mage["power"],
        "min_power": min_mage["power"],
        "average_power": average
        }
    return new_dict


def print_list(
        example_list: list[dict[str, Any]]) -> None:

    for artifact in example_list:
        print(
            f'{artifact["name"]} '
            f'({artifact["power"]})'
        )


def print_names(example_list: list[str]) -> None:
    for name in example_list:
        print(name)


def print_stats_dict(examp: dict[str, Any]) -> None:
    print(
        f"Max: {examp['max_power']},\n"
        f"Min: {examp['min_power']},\nAverage: {examp['average_power']}\n"
    )


def test_sorter() -> None:
    examp_dict1 = {
        "name": "Sumeyye",
        "power": 22,
        "type": "Computer Engineering"
        }
    examp_dict2 = {
        "name": "Ayse",
        "power": 43,
        "type": "Security"
        }
    examp_dict3 = {
            "name": "Hamza",
            "power": 21,
            "type": "Electric Engineering"
        }
    examp_dict4 = {
            "name": "Merve",
            "power": 23,
            "type": "Pharmacy"
        }
    examp_dict5 = {
            "name": "Abit",
            "power": 45,
            "type": "Cooker"
        }
    examp_dict6 = {
            "name": "Enes",
            "power": 20,
            "type": "Lawyer"
        }
    examp_list = [
        examp_dict1, examp_dict2, examp_dict3,
        examp_dict4, examp_dict5, examp_dict6
        ]
    sorted_list = artifact_sorter(examp_list)
    print_list(sorted_list)


def test_filter() -> None:
    examp_dict1 = {
        "name": "Sumeyye",
        "power": 22,
        "element": "fire"
        }
    examp_dict2 = {
        "name": "Ayse",
        "power": 43,
        "element": "water"
        }
    examp_dict3 = {
            "name": "Hamza",
            "power": 21,
            "element": "air"
        }
    examp_dict4 = {
            "name": "Merve",
            "power": 23,
            "element": "gold"
        }
    examp_dict5 = {
            "name": "Abit",
            "power": 45,
            "element": "fire"
        }
    examp_dict6 = {
            "name": "Enes",
            "power": 20,
            "element": "water"
        }
    examp_list = [
        examp_dict1, examp_dict2, examp_dict3,
        examp_dict4, examp_dict5, examp_dict6
        ]
    filtered_list = power_filter(examp_list, 20)
    print_list(filtered_list)


def test_map() -> None:
    examp_list = ["Ayse", "Abit", "Sumeee"]
    spell_name_list = spell_transformer(examp_list)
    print_names(spell_name_list)


def test_stats() -> None:
    examp_dict1 = {
        "name": "Sumeyye",
        "power": 22,
        "type": "Computer Engineering"
        }
    examp_dict2 = {
        "name": "Ayse",
        "power": 43,
        "type": "Security"
        }
    examp_dict3 = {
            "name": "Hamza",
            "power": 21,
            "type": "Electric Engineering"
        }
    examp_dict4 = {
            "name": "Merve",
            "power": 23,
            "type": "Pharmacy"
        }
    examp_dict5 = {
            "name": "Abit",
            "power": 45,
            "type": "Cooker"
        }
    examp_dict6 = {
            "name": "Enes",
            "power": 20,
            "type": "Lawyer"
        }
    examp_list = [
        examp_dict1, examp_dict2, examp_dict3,
        examp_dict4, examp_dict5, examp_dict6
        ]
    stat_dict = mage_stats(examp_list)
    print_stats_dict(stat_dict)


def main() -> None:
    test_sorter()
    print("\n=================================\n")
    test_filter()
    print("\n=================================\n")
    test_map()
    print("\n=================================\n")
    test_stats()
    print()


if __name__ == "__main__":
    main()
