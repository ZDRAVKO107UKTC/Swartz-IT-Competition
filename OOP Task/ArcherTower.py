from DefenceStructure import DefenceStructure
from Castle import CastleTower

class ArcherTower(DefenceStructure):
    def __init__(self, name, health, range):
        super().__init__(name, health)
        self.range = range

    def attack(self):
        return f"{self.name} Attacks enemies from {self.range} meters" #i used meters for example

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return f"{self.name} has been destroyed!"
        return f"{self.name} took {amount} damage. {self.health} health remaining."

    def repair(self):
        self.health += 10
        return f"{self.name} has been repaired. Current health: {self.health}."

    def defend(self, castle):
        if not isinstance(castle, CastleTower):
            return "Not an object"
        # проверка за това дали има обект и след това проверявам дали обекта е жив

        if self.health > 0:
            return f"{self.name} defending {castle.name}, targeting enemies {self.range} meters"
        else:
            return f"destroyed castle"

