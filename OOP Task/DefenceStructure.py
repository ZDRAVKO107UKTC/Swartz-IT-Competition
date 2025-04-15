from abc import ABC, abstractmethod

class DefenceStructure(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def take_damage(self, amount):
        pass

    @abstractmethod
    def repair(self):
        pass
