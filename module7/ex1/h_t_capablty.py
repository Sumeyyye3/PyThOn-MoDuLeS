from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str):
        pass


class TransformCapability(ABC):
    def __init__(self) -> str:
        self.flag = 0

    @abstractmethod
    def transform(self) -> str:
        pass
    
    @abstractmethod
    def revert(self) -> str:
        pass
