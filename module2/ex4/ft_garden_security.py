#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def grow(self) -> None:
        self._height = round(self._height + 0.8, 1)

    def set_age(self, value: int) -> None:
        if value >= 0:
            self._age = value
            print(f"Age updated: {value} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value >= 0:
            self._height = value
            print(f"Height updated: {round(value)}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_height(self) -> float:
        return self._height

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-10.0)
    rose.set_age(-5)
    print()
    print("Current state:", end=" ")
    rose.show()
