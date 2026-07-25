from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy
from ex2 import DefensiveStrategy, BattleStrategy
from ex2 import WrongStrategyError


def main():
    members = [
        (FlameFactory(), NormalStrategy()),
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),

        (FlameFactory(), DefensiveStrategy()),
        (AquaFactory(), AggressiveStrategy()),
    ]
    battle(members)




def battle(members: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    for i in range(len(members)):
        for j in range(i + 1, len(members)):

            factory1, strategy1 = members[i]
            factory2, strategy2 = members[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

        print(f"[ ({creature1.describe()}+{creature2.describe()}) ]")

        try:
            strategy1.act(creature1)
        except WrongStrategyError as e:
            print(e)

        try:
            strategy2.act(creature2)
        except WrongStrategyError as e:
            print(e)


if __name__ == "__main__":
    main()
