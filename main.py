import sys
import random
import pickle



def switch(x):
    match x:
        case "equip sword":
            print(Sword.name, "equipped")
            player.equip.append(Sword)
            print(player.dmg)
            player.dmg += Sword.dmg
            print(player.dmg)

        case "equip shield":
            print("Shield equipped")
            player.equip.append(Shield)

        case "equip":
            print(player.inventory)
            print("You can equip", player.inventory, "\nand you have", player.equip, "equiped")
            command = input("What item you want to equip?")
            
        case "drop":    
            i = len(items)
            index = random.randint(0, i - 1)
            item = items[index]
            items.remove(item)
            player.inventory.append(item)
            print("You got", getattr(item, "name"))
            print(player.inventory)

        case _:
            print("Wrong argument, try again")



def save():
    with open("game\items", "wb") as file:
        pickle.dump(items, file)

    with open("game\player", "wb") as file:
        pickle.dump(player, file)

    with open("game/firstRun", "w") as file:
        file.write("False")

def load():
    with open("game/firstRun", "r") as file:
        firstRun = file.read

    if firstRun == "False":
        with open("game/items", "rb") as file:
            items = pickle.load(file)
        
        with open("game/player", "rb") as file:
            player = pickle.load(file)

class Player:
    hp: int 
    equip: list
    inventory: list
    dmg: int 
    weaponEquiped: False
    shieldEquiped: False

    def playerHeal(self, heal):
        self.hp += heal

    def playerTakeDamage(self, damage):
        self.hp -= damage

    def increasePlayerDamage(self, damage):
        self.dmg += damage

    def increasePlayerHp(self, hp):
        self.hp += hp

    def decreasePlayerDamage(self, damage):
        self.dmg -= damage

    def decreasePlayerHp(self, hp):
        self.hp -= hp



class Weapon:
    name: str 
    dmg: int
    armor: 0


class DefenceItem:
    name: str 
    armor: int 
    dmg: 0


class Monster:
    name: str
    dmg: int
    hp: int

    def monsterTakeDamage(self, damage):
        self.hp -= damage


Sword = Weapon()
Sword.name = "One-handed sword"
Sword.dmg = 10  


Shield = DefenceItem()
Shield.name = "Shield"
Shield.armor = 10


player = Player()
player.hp = 100
player.equip = []
player.inventory = []
player.dmg = 1


items = []
items.append(Sword)
items.append(Shield)

load()

commnad = input()
switch(commnad.lower())


if len(player.inventory) > 0:
    player.inventory = sorted(player.inventory)

if len(player.equip) > 0:
    player.equip = sorted(player.equip)

save()
