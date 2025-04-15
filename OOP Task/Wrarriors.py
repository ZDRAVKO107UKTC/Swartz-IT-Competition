from WarriorsExample import WarriorExample


class Warriors(WarriorExample):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def attack(self, target):
        if not isinstance(target, WarriorExample):
            raise ValueError(f"Target must be a Warrior instance, not {type(target).__name__}")

        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.health -= self.attack_power

        if target.health <= 0:
            target.health = 0
            print(f"{target.name} has been defeated!")
        else:
            print(f"{target.name} now has {target.health} health remaining.")
