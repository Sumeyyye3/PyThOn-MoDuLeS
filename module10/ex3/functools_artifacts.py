from functools import lru_cache, partial, reduce, singledispatch
from operator import add, mul
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(operations[operation], spells)


def base_enchantment(
    power: int,
    element: str,
    target: str,
) -> str:
    return (
        f"{element.capitalize()} enchantment with "
        f"{power} power cast on {target}"
    )


def partial_enchanter(
    base_enc: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    fire_enchantment = partial(
        base_enc,
        50,
        "fire",
    )

    ice_enchantment = partial(
        base_enc,
        50,
        "ice",
    )

    lightning_enchantment = partial(
        base_enc,
        50,
        "lightning",
    )

    return {
        "fire": fire_enchantment,
        "ice": ice_enchantment,
        "lightning": lightning_enchantment,
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci number cannot be negative")

    if n < 2:
        return n

    return (
        memoized_fibonacci(n - 1)
        + memoized_fibonacci(n - 2)
    )


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def test_spell_reducer() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(
        f"Product: "
        f"{spell_reducer(spells, 'multiply')}"
    )
    print(f"Max: {spell_reducer(spells, 'max')}")


def test_partial_enchanter() -> None:
    print("\nTesting partial enchanter...")
    enc = partial_enchanter(base_enchantment)
    print(enc["fire"]("Dragon"))
    print(enc["ice"]("Knight"))
    print(enc["lightning"]("Wizard"))


def test_memoized_fibonacci() -> None:
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


def test_spell_dispatcher() -> None:
    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher({"spell": "unknown"}))


def main() -> None:
    test_spell_reducer()
    test_partial_enchanter()
    test_memoized_fibonacci()
    test_spell_dispatcher()


if __name__ == "__main__":
    main()
