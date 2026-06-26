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
        self._height = round(self._height + 2.1, 1)

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


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, t_meter: float) -> None:
        super().__init__(name, height, age)
        self.t_meter = t_meter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of ", end="")
        print(f"{self._height}cm long and ", end="")
        print(f"{self.t_meter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.t_meter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, hv_season: str) -> None:
        super().__init__(name, height, age)
        self.hv_season = hv_season
        self.nutritional_value = 0

    def set_age(self, value: int) -> None:
        if value >= self._age:
            diff = value - self._age
            self.nutritional_value += diff
            self._age = value

    def set_height(self, value: float) -> None:
        if value >= 0:
            self._height = value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.hv_season}")
        print(f" Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.set_age(tomato.get_age() + 1)
    tomato.show()
