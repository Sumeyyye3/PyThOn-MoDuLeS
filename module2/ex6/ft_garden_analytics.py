#!/usr/bin/env python3

class Plant:
    class NestedInfo:
        def __init__(self) -> None:
            self._grow_nb = 0
            self._age_nb = 0
            self._show_nb = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_nb} grow, ", end="")
            print(f"{self._age_nb} age, ", end="")
            print(f"{self._show_nb} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        self._stats = Plant.NestedInfo()

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def set_height(self, value: float) -> None:
        if value >= 0:
            self._height = value

    def grow(self) -> None:
        self._stats._grow_nb += 1
        self._height = round(self._height + 8, 1)

    def age(self, value: int) -> None:
        self._stats._age_nb += 1
        if value >= 0:
            self._age = value
        else:
            print(f"{self._name}: Error, age can't be negative")

    def show(self) -> None:
        self._stats._show_nb += 1
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def show_stats(self) -> None:
        self._stats.display()

    @staticmethod
    def is_age(age: int) -> bool:
        return age > 365

    @classmethod
    def is_unknown(obj) -> "Plant":
        return obj("Unknown plant", 0.0, 0)

    def get_stats(self) -> "Plant.NestedInfo":
        return self._stats


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed_number = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed_number = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed_number}")


class Tree(Plant):
    class NestedInfo(Plant.NestedInfo):
        def __init__(self) -> None:
            super().__init__()
            self._shade_nb = 0

    def __init__(self, name: str, height: float, age: int, t_meter: float) -> None:
        super().__init__(name, height, age)
        self._stats = Tree.NestedInfo()
        self.t_meter = t_meter

    def show_stats(self) -> None:
        self._stats.display()
        print(f" {self._stats._shade_nb} shade")

    def produce_shade(self) -> None:
        self._stats._shade_nb += 1
        print(f"Tree {self._name} now produces a ", end="")
        print(f"shade of {self._height}cm long ", end="")
        print(f"and {self.t_meter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.t_meter}cm")


def showmen(obje: Plant) -> None:
    obje.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_age(400)}")
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[statistics for Rose]")
    showmen(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    showmen(rose)
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    showmen(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    showmen(oak)
    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.set_height(110.0)
    sunflower.age(65)
    sunflower.bloom()
    sunflower.show()
    print("[statistics for Sunflower]")
    showmen(sunflower)
    print("\n=== Anonymous")
    anon = Plant.is_unknown()
    anon.show()
    print("[statistics for Unknown plant]")
    showmen(anon)
