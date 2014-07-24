# -*- coding: utf-8 -*-
import random

global EntityId
global players

class Player():
    owner = None

    #Vitals
    health = 100
    mana = 100
    stamina = 100

    #Core Scroes
    strength = 1      # str skills / 3
    constitution = 1  # con skills / 3
    dexterity = 1     # dex skills / 3
    agility = 1       # agi skills / 3
    intellegence = 1  # int skills / 3
    wisdom = 1        # wis skills / 3

    #strength skills

    focus = 1         # accuracy - rewarded on hit
    steelarm = 1      # damage bonus (stat/6) = bonus damage, rewarded when getting top end of damage roll

    #constitution skills
    parry = 1 # rewarded on parry
    block = 1 # stat # rewarded on block
    ironskin = 1 # + max health # rewarded on taking a physical hit

    #dexterity skills
    powershot = 1 #damage with ranged (exp when top half of damage range)
    accurateshot = 1 #accuracy with ranged (exp on hit)

    #basic battle stats
    attack = 10
    defense = 10
    minDam = 1
    maxDam = 6

    def __init__(self, owner):
        self.entity = owner

    def attacks(self, target):
        modifier = self.attack / target.defense
        damage = random.randint(self.minDam, self.maxDam) * modifier
        return damage
