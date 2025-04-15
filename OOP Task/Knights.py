from WarriorsExample import WarriorExample
from Castle import CastleTower
from DefenceStructure import DefenceStructure



class Knights(WarriorExample):
    def __init__(self, name, health, attack_power, armour, weapon):
        super().__init__(name, health, attack_power)
        self.armour = armour
        self.weapon = weapon

    def attack(self, target):
        if not isinstance(target, DefenceStructure):
            return "Not a defence object"

        damage = self.attack_power
        result = target.take_damage(damage)

        return f"{self.name} attacks {target.name} with {self.weapon}, dealing {damage} damage. {result}"

    def defend(self, target):
        if not isinstance(target, CastleTower):
            return "Not a castle object"


        if self.armour > 50:
            print(f"the Knight: {self.name} stands strong at the gates of {target.name}")

        target.add_defender(self.name)
        return f"{self.name} is defending {target.name} with armour {self.armour}"

    def fight(self, target):

        if not isinstance(target, WarriorExample):
            return "Invalid target. The target is not a Warrior."

        print(f"{self.name} in battle with {target.name}")


        while self.health > 0 and target.health > 0:

            print(f"{self.name} attacks {target.name} with {self.weapon} dealing {self.attack_power} damage")
            target.health -= self.attack_power


            if target.health <= 0:
                return "Victory"

            incoming_damage = target.attack_power
            print(f"{target.name} strikes back dealing {incoming_damage} damage")

            if self.armour > 0:
                if self.armour >= incoming_damage:
                    self.armour -= incoming_damage
                    print(f"{self.name}'s armour  Remaining armour: {self.armour}")
                else:
                    leftover_damage = incoming_damage - self.armour
                    self.armour = 0
                    self.health -= leftover_damage
                    print(f"{self.name} armour is broken health: {self.health}")
            else:
                self.health -= incoming_damage
                print(f"{self.name} takes a hit Remaining health {self.health}")

            if self.health <= 0:
                return "Defeat"
