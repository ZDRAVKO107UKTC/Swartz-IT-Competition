from Knights import Knights
from Castle import CastleTower
from ArcherTower import ArcherTower

castle = CastleTower(name="Iron Keep", health=500, drawbridge=True)
archer_tower = ArcherTower(name="North Tower", health=150, range=50)

castle.add_tower(archer_tower.name)

attacker1 = Knights(name="Knight of Shadows", health=120, attack_power=35, armour=50, weapon="Shadow Blade")
attacker2 = Knights(name="Flame Knight", health=100, attack_power=40, armour=40, weapon="Flame Sword")

castle_defender = Knights(name="Castle Defender", health=150, attack_power=30, armour=60, weapon="Guardian Spear")

defense_action = castle_defender.defend(castle)
print(defense_action)

print("\nBegins")

result = attacker1.attack(archer_tower)
print(result)

while True:
    fight_result = castle_defender.fight(attacker1)
    print(fight_result)
    if fight_result == "Victory" or fight_result == "Defeat":
        break

while True:
    fight_result = attacker2.fight(castle_defender)
    print(fight_result)
    if fight_result == "Victory" or fight_result == "Defeat":
        break

castle_repair = castle.repair()
print(castle_repair)


print("\nFinal")
print(f"{castle.name}: {castle.health} health remaining")
print(f"{archer_tower.name}: {archer_tower.health} health remaining")
print(f"{attacker1.name}: {attacker1.health} health, {attacker1.armour} armour remaining")
print(f"{attacker2.name}: {attacker2.health} health, {attacker2.armour} armour remaining")
print(f"{castle_defender.name}: {castle_defender.health} health, {castle_defender.armour} armour remaining")
