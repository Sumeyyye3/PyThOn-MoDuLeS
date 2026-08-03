from typing import Callable


def fireball(target: str, power: int) -> str:
    msg = f"Fireball hits {target} with {power} damage"
    return msg


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        result_one = spell1(target, power)
        result_two = spell2(target, power)
        results = result_one, result_two
        return results

    return combined_spell


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    def amplified_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)

    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    def sequence_spell(target: str, power: int) -> list[str]:
        results = []

        for spell in spells:
            results.append(spell(target, power))

        return results

    return sequence_spell


def main() -> None:
    print("Testing spell combiner...")

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)

    print(
        f"Combined spell result: "
        f"{result[0].replace(' with 10 damage', '')}, "
        f"Heals Dragon"
    )

    print("\nTesting power amplifier...")

    mega_fireball = power_amplifier(fireball, 3)

    original_power = 10
    amplified_result = mega_fireball("Dragon", original_power)

    print(f"Original: {original_power}, Amplified: {original_power * 3}")
    print(amplified_result)

    print("\nTesting conditional caster...")

    def strong_target(target: str, power: int) -> bool:
        return power >= 50

    conditional_fireball = conditional_caster(
        strong_target,
        fireball
    )

    print(conditional_fireball("Dragon", 100))
    print(conditional_fireball("Dragon", 20))

    print("\nTesting spell sequence...")

    sequence = spell_sequence(
        [fireball, heal]
    )

    results = sequence("Knight", 80)

    for spell_result in results:
        print(spell_result)


if __name__ == "__main__":
    main()
