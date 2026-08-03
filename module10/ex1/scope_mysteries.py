from typing import Callable, Any

def mage_counter() -> Callable:
    i = 0

    def counter() -> int:
        nonlocal i
        i += 1
        return i

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def sum_power(total: int) -> int:
        nonlocal power
        power += total
        return power

    return sum_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def factory(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return factory


def memory_vault() -> dict[str, Callable]:
    memory = {}
    def store(k: str, v: Any) -> None:
        memory[k] = v

    def recall(k: str) -> Any:
        if memory.get(k) is None:
            return "Memory not found"
        else:
            return memory.get(k)

    callab_dict = {
        "store": store,
        "recall": recall
        }
    return callab_dict


def test_mage_counter() -> None:
    print("Testing mage counter...")

    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("Testing spell accumulator...")

    accumulator = spell_accumulator(100)

    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")


def test_enc_factory() -> None:
    print("Testing enchantment factory...")

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")

    print(flaming("Sword"))
    print(frozen("Shield"))



def test_memory() -> None:
    print("Testing memory vault...")

    vault = memory_vault()

    vault["store"]("secret", 42)

    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")



def test_spell_ac() -> None:
    print("Testing spell accumulator...")

    accumulator = spell_accumulator(100)

    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")
    print(f"Base 100, add 50: {accumulator(50)}")

def main():

    test_mage_counter()
    print("\n=====================================\n")
    test_spell_ac()
    print("\n=====================================\n")
    test_enc_factory()
    print("\n=====================================\n")
    test_memory()
    


if __name__ == "__main__":
    main()
