from ex0.creature import Creature
from .h_t_capablty import HealCapability
from .h_t_capablty import TransformCapability


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Blomelle", "Grass/Fairy")

    def heal(self) -> str:
        return f"{self.name} heals itself and others for a large amount"

    def attack(self) -> str:
        return f"{self.name} uses Petal Dance"


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return f"{self.name} uses Vine Whip!"

    def heal(self) -> str:
        return f"{self.name} heals itself for a small amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.flag:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def revert(self) -> str:
        self.flag = 0
        return f"{self.name} returns to normal."

    def transform(self) -> str:
        self.flag = 1
        return f"{self.name} shifts into a sharper form!"


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self.flag:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def revert(self) -> str:
        self.flag = 0
        return f"{self.name} stabilizes its form."

    def transform(self) -> str:
        self.flag = 1
        return f"{self.name} morphs into a dragonic battle form!"
