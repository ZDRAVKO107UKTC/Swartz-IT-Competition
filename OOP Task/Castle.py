from DefenceStructure import DefenceStructure

class CastleTower(DefenceStructure):
    def __init__(self, name, health, drawbridge):
        super().__init__(name, health)
        self.drawbridge = drawbridge
        self.defenders = []
        self.towers = []

    def attack(self):
        return f"{self.name} Attacks the enemies!"

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            return f"{self.name} is destroyed!"
        return f"{self.name} took {amount} damage: {self.health} remaining"

    def repair(self):
        self.health += 20
        return f"{self.name} has been repaired Current: {self.health}"


    def add_defender(self, defender):
        self.defenders.append(defender)
        return f"{defender} added. Current : {self.defenders}"

    def remove_defender(self, defender):
        if defender in self.defenders:
            self.defenders.remove(defender)
            return f"{defender} removed:  Current: {self.defenders}"
        return "Defender not found"

    def add_tower(self, tower):
        self.towers.append(tower)
        return f"{tower} added Current : {self.towers}"

    def remove_tower(self, tower):
        if tower in self.towers:
            self.towers.remove(tower)
            return f"{tower} removed: Current: {self.towers}"
        return f"{tower} not found among towers"

