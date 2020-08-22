
# Soldier
class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage
        

            
# Viking
class Viking(Soldier):

    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        
    def receiveDamage(self, damage):
        self.health -= damage 
        if self.health > 0: 
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
      
# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

     
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0: 
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# # War  
 
class War:
    def __init__(self):
         self.vikingArmy = []
         self.saxonArmy = []
    

def addViking(Viking):
    vikingArmy.append(Viking)


def addSaxon(Saxon):
    saxonArmy.append(Saxon)


def vikingAttack(self):
    Saxon.receiveDamage = Viking.strenght
    saxonArmy -= 1
    return Saxon.receiveDamage, Saxon.strenght

def saxonAttack():
    Viking.receiveDamage = Saxon.strenght
    saxonArmy -= 1
    return Viking.receiveDamage, Viking.strenght

def showStatus():
    if len(saxonArmy) == 0:
        return "Vikings have won the war of the century!"
    elif len(vikingArmy) == 0:
        return "Saxons have fought for their lives and survive another day..."
    elif len(SanxonArmy) > 0 and len(vikingArmy) > 0:
        return "Vikings and Saxons are still in the thick of battle."




# class Viking:
#     pass

# # Saxon


# class Saxon:
#     pass

# # War


# class War:
#     pass
