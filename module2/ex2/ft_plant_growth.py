#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age_age(self) -> None:
        self.age = self.age + 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_plant_grow() -> None:
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    start_height = rose.height
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age_age()
        rose.show()
    total_height = round((rose.height - start_height), 1)
    print(f"Growth this week: {total_height}cm")


if __name__ == "__main__":
    ft_plant_grow()
