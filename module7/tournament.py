from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy
from ex2 import DefensiveStrategy, BattleStrategy
from ex2 import WrongStrategyError


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")

    battles([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print("\n\n\n")
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")

    battles([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print("\n\n\n")
    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

    battles([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])


def battles(members: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(members)} opponents involved")
    for i in range(len(members)):
        factory1, strategy1 = members[i]
        for j in range(i + 1, len(members)):
            factory2, strategy2 = members[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *\n")
            print(f"{creature1.describe()}")
            print("vs.")
            print(f"{creature2.describe()}")
            print(" now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)
            except WrongStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    main()
