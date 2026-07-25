from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.h_t_capablty import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self) -> None:
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class WrongStrategyError(Exception):
    pass


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise WrongStrategyError(
                f"Invalid Creature '{creature.name} for this normal strategy")

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise WrongStrategyError(
                f"Invalid Creature '{creature.name}'\
 for this aggressive strategy")
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())

    def is_valid(self, creature: Creature) -> bool:
        flag = isinstance(creature, TransformCapability)
        return flag


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise WrongStrategyError(
                f"Invalid Creature '{creature.name}'\
 for this defensive strategy")

        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())

    def is_valid(self, creature: Creature) -> bool:
        flag = isinstance(creature, HealCapability)
        return flag
