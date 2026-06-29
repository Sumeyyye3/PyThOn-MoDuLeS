import alchemy


def main() -> None:
    print("\n=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    msg = alchemy.create_air()
    print(f"Testing create_air: {msg}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")

    print("Testing the hidden create_earth: ", end="")
    print(f"{alchemy.create_earth()}")
