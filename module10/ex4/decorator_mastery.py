from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar
import time


T = TypeVar("T")


def spell_timer(func: Callable[..., T]) -> Callable[..., T]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - start
        print(
            f"Spell completed in {elapsed_time:.3f} seconds"
        )

        return result

    return wrapper


def power_validator(
    min_power: int
) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(
        func: Callable[..., str]
    ) -> Callable[..., str]:
        @wraps(func)
        def wrapper(
            *args: Any,
            **kwargs: Any
        ) -> str:
            power = kwargs.get("power")
            if power is None:
                power = args[-1]

            if not isinstance(power, int):
                return "Insufficient power for this spell"

            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int
) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(
        func: Callable[..., str]
    ) -> Callable[..., str]:
        @wraps(func)
        def wrapper(
            *args: Any,
            **kwargs: Any
        ) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/"
                            f"{max_attempts})"
                        )

            return (
                "Spell casting failed after "
                f"{max_attempts} attempts"
            )

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(
                character.isalpha()
                or character.isspace()
                for character in name
            )
        )

    @power_validator(10)
    def cast_spell(
        self,
        spell_name: str,
        power: int
    ) -> str:
        return (
            f"Successfully cast {spell_name} "
            f"with {power} power"
        )


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(3)
def failed_spell() -> str:
    raise RuntimeError("Spell failed")


def successful_spell() -> str:
    return "Waaaaaaagh spelled !"


def test_spell_timer() -> None:
    print("\nTesting spell timer...")
    result = fireball()
    print(f"Result: {result}")


def test_retrying_spell() -> None:
    print("\nTesting retrying spell...")
    failed_result = failed_spell()
    print(failed_result)
    successful_result = successful_spell()
    print(successful_result)


def test_mage_guild() -> None:
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(
        MageGuild.validate_mage_name(
            "Merlin"
        )
    )

    print(
        MageGuild.validate_mage_name(
            "M3"
        )
    )

    print(
        guild.cast_spell(
            "Lightning",
            15
        )
    )

    print(
        guild.cast_spell(
            "Lightning",
            5
        )
    )


def main() -> None:
    test_spell_timer()
    test_retrying_spell()
    test_mage_guild()


if __name__ == "__main__":
    main()
