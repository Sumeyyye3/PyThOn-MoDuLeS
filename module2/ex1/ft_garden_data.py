#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("Rose", 25.0, 30)
    sun_flower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    rose.show()
    sun_flower.show()
    cactus.show()


if __name__ == "__main__":
    ft_garden_data()
