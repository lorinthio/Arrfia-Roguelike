# -*- coding: utf-8 -*-

class Monster:

    def __init__(self, size, STR, CON, DEX, AGI, WIS, INT, name=''):
        self.name = name
        self.StatCreation(size, STR, CON, DEX, AGI, WIS, INT)

    def StatCreation(self, size, strength, constitution, dexterity, agility, wisdom, intellegence):
        if size == 'small':
            health = strength * 1
            health2 = constitution * 1.5
            health = int(health)
            health2 = int(health2)
            health = health + health2
            attack = strength * 2
            strdmg = strength / 10.0
            strdmg = int(strdmg)
            defence = constitution * 1.5
            self.strdmg = strdmg
            self.health = health
            self.attack = attack
            self.defence = defence
            dexterity = dexterity
            agility = agility
            accuracy = dexterity * 2.5
            accuracy = accuracy + 50
            speedmod = agility + dexterity
            speedmod = speedmod / 220.00
            speedmod = 1 - speedmod
            dodge = agility * 3
            critical = dexterity / 3.6
            critical1 = agility / 3.6
            critical = critical + critical1
            critical = int(critical)
            self.speed = speedmod
            self.accuracy = accuracy
            self.dodge = dodge
            self.critical = critical
            wisdom = wisdom
            intellegence = intellegence
            mana = wisdom * 2
            mana2 = intellegence * 2
            mana2 = int(mana2)
            mana = mana + mana2
            mattack = intellegence * 2
            mdefence = wisdom * 2
            self.mana = mana
            self.mattack = mattack
            self.mdefence = mdefence

            #speed calculations
            self.moveSpeed = int(20.000 * (1.000 - ((agility + dexterity) / 120.000)))
        elif size == "medium":
            health = strength * 2
            health2 = constitution * 2
            health = int(health)
            health2 = int(health2)
            health = health + health2
            attack = strength * 3
            strdmg = strength / 8.0
            strdmg = int(strdmg)
            defence = constitution * 2
            self.strdmg = strdmg
            self.health = health
            self.attack = attack
            self.defence = defence
            dexterity = dexterity
            agility = agility
            accuracy = dexterity * 2
            accuracy = accuracy + 50
            speedmod = agility + dexterity
            speedmod = speedmod / 250.00
            speedmod = 1 - speedmod
            dodge = agility * 2
            critical = dexterity / 4.0
            critical1 = agility / 4.0
            critical = critical + critical1
            critical = int(critical)
            self.speed = speedmod
            self.accuracy = accuracy
            self.dodge = dodge
            self.critical = critical
            wisdom = wisdom
            intellegence = intellegence
            mana = wisdom * 2
            mana2 = intellegence * 2
            mana2 = int(mana2)
            mana = mana + mana2
            mattack = intellegence * 2
            mdefence = wisdom * 2
            self.mana = mana
            self.mattack = mattack
            self.mdefence = mdefence

            self.moveSpeed = int(24.000 * (1.000 - ((agility + dexterity) / 100.000)))
        elif size == "large":
            health = strength * 3
            health2 = constitution * 2
            health = int(health)
            health2 = int(health2)
            health = health + health2
            attack = strength * 3
            strdmg = strength / 7.0
            strdmg = int(strdmg)
            defence = constitution * 2.4
            self.strdmg = strdmg
            self.health = health
            self.attack = attack
            self.defence = defence
            dexterity = dexterity
            agility = agility
            accuracy = dexterity * 1.6
            accuracy = accuracy + 50
            speedmod = agility + dexterity
            speedmod = speedmod / 280.00
            speedmod = 1 - speedmod
            dodge = agility * 1.5
            critical = dexterity / 5
            critical1 = agility / 5
            critical = critical + critical1
            critical = int(critical)
            self.speed = speedmod
            self.accuracy = accuracy
            self.dodge = dodge
            self.critical = critical
            wisdom = wisdom
            intellegence = intellegence
            mana = wisdom * 2
            mana2 = intellegence * 2
            mana2 = int(mana2)
            mana = mana + mana2
            mattack = intellegence * 2
            mdefence = wisdom * 2
            self.mana = mana
            self.mattack = mattack
            self.mdefence = mdefence

            self.moveSpeed = int(30.000 * (1.000 - ((agility + dexterity) / 80.000)))

        elif size == "boss":
            health = strength * 4
            health2 = constitution * 5
            health = int(health)
            health2 = int(health2)
            health = health + health2
            attack = strength * 3.5
            strdmg = strength / 6.0
            strdmg = int(strdmg)
            defence = constitution * 3.5
            self.strdmg = strdmg
            self.health = health
            self.attack = attack
            self.defence = defence
            dexterity = dexterity
            agility = agility
            accuracy = dexterity * 2.5
            accuracy = accuracy + 60
            speedmod = agility + dexterity
            speedmod = speedmod / 300.00
            speedmod = 1 - speedmod
            dodge = agility * 1.5
            critical = dexterity / 4
            critical1 = agility / 4
            critical = critical + critical1
            critical = int(critical)
            self.speed = speedmod
            self.accuracy = accuracy
            self.dodge = dodge
            self.critical = critical
            wisdom = wisdom
            intellegence = intellegence
            mana = wisdom * 3
            mana2 = intellegence * 3
            mana2 = int(mana2)
            mana = mana + mana2
            mattack = intellegence * 3
            mdefence = wisdom * 3
            self.mana = mana
            self.mattack = mattack
            self.mdefence = mdefence

            self.moveSpeed = int(25.000 * (1.000 - ((agility + dexterity) / 150.000)))

        print("Name: " + self.name + "Speed : " + str(self.moveSpeed))