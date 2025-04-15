from abc import ABC, abstractmethod


class WarriorExample(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self):
        pass

