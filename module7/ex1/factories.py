from ex0.creature import Creature
from ex0.factory import CreatureFactory
from ex1.creatures import Morphagon, Bloomelle
from ex1.creatures import Shiftling, Sproutling


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        shiftlg = Shiftling()
        return shiftlg

    def create_evolved(self) -> Creature:
        morp = Morphagon()
        return morp


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        sptl = Sproutling()
        return sptl

    def create_evolved(self) -> Creature:
        bloomel = Bloomelle()
        return bloomel
