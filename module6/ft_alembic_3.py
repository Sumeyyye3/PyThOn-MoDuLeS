from alchemy.elements import create_air


def main() -> None:
    print("\n\n====== Alembic 3 ======\n")
    print(
        "Accessing alchemy/elements.py using "
        "'from ... import ...' structure"
    )
    print(create_air())


if __name__ == "__main__":
    main()
