from ex0.factory import CreatureFactory
from ex1.creatures import Morphagon, Bloomelle
from ex1.creatures import Shiftling, Sproutling


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        shiftlg = Shiftling()
        return shiftlg

    def create_evolved(self) -> Morphagon:
        morp = Morphagon()
        return morp


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Sproutling:
        sptl = Sproutling()
        return sptl

    def create_evolved(self) -> Bloomelle:
        bloomel = Bloomelle()
        return bloomel
