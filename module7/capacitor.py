from ex1.factories import HealingCreatureFactory
from ex1.factories import TransformCreatureFactory


def test_heal(factory: HealingCreatureFactory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(f"{base.describe()}")
    print(base.attack())
    print(base.heal())

    print("\n\n\n")
    print(" evolved:")
    print(f"{evolved.describe()}")
    print(evolved.attack())
    print(evolved.heal())

def test_transform(factory: TransformCreatureFactory):
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(f"{base.describe()}")
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print("\n\n\n")
    print(" evolved:")
    print(f"{evolved.describe()}")
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())

def main():
    heal = HealingCreatureFactory()
    test_heal(heal)

    print("\n----------------------------------------\n")

    transform = TransformCreatureFactory()
    test_transform(transform)


if __name__ == "__main__":
    main()
