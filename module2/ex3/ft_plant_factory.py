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


def ft_plant_factory() -> None:
    obj_one = Plant("Rose", 25.0, 30)
    obj_two = Plant("Oak", 200.0, 365)
    obj_three = Plant("Cactus", 5.0, 90)
    obj_four = Plant("Sunflower", 80.0, 45)
    obj_five = Plant("Fern", 15.0, 120)

    plant_list = [obj_one, obj_two, obj_three, obj_four, obj_five]
    print("=== Plant Factory Output ===")
    for i in range(5):
        print("Created:", end=" ")
        plant_list[i].show()


if __name__ == "__main__":
    ft_plant_factory()
