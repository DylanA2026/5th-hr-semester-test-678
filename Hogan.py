#Name: Hogan McCune
#Class: 5th Hour
#Assignment: Semester Project 2

#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but they want you to work together as a team
#under agile development and document your work under weekly sprints. You will designate a team lead,
#who is dedicated to putting the code all together and maintaining it, and a scrum master who will
#document the progression of the project.

#You have until the end of the week before finals week is due to brainstorm an idea together, and then
#turn that idea into functioning code. The code itself must have at least: 1 class, 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total, nor do
#nested if statements),1 variable with a user input, and 1 form of an assignment operator. You are free
#to add whatever else you feel is necessary to complete your concept. You will be graded based on how
#those ideas are implemented together and your overall contribution to the team.

import time
import random

def intro():
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXX")
    time.sleep(1)
    print("XXXXXXX")
    time.sleep(1)
    print("XXXXXX")
    time.sleep(1)
    print("XXXXX")
    time.sleep(1)
    print("XXXX")
    time.sleep(1)
    print("XXX")
    time.sleep(1)
    print("XX")
    time.sleep(1)
    print("X")
    time.sleep(1)
    print("XX")
    time.sleep(1)
    print("XXX")
    time.sleep(1)
    print("XXXX")
    time.sleep(1)
    print("XXXXX")
    time.sleep(1)
    print("XXXXXX")
    time.sleep(1)
    print("XXXXXXX")
    time.sleep(1)
    print("XXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXXXXX")
    time.sleep(1)
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")

intro()

def randompick():
    global enemyfirst
    global alliesfirst
    enemyfirst = False
    alliesfirst = False
    pick = random.randint(0,1)
    if pick == 0:
        enemyfirst = True
    else:
        alliesfirst = True

choose_ally = 0

def enemyatk():
    choose_ally == random.randint(1,3)
    if choose_ally == 1:
        Federation_Soldier.msAtk()
    elif choose_ally == 2:
        Federation_Medic.mmAtk()
    elif choose_ally == 3:
        Federation_literaltank.mtAtk()

class character:
    def __init__(self, name, hp, attack, maxhp, defensebull):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.maxhp = maxhp
        self.defensebull = defensebull
    def heal(self):
        self.hp = self.hp + random.randint(20, 30)
        if self.hp > self.maxhp:
            self.hp = self.maxhp


    def fs_atk(self):
        Federation_Soldier.attack = random.randint(8,15)
        crit = random.randint(1,20)
        if crit == 20:
            Federation_Soldier.attack = Federation_Soldier.attack * 2
            self.hp = self.hp - Federation_Soldier.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_Soldier.attack

    def fm_atk(self):
        Federation_Medic.attack = random.randint(2,5)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_Medic.attack = Federation_Medic.attack * 2
            self.hp = self.hp - Federation_Medic.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_Medic.attack

    def ft_atk(self):
        Federation_literaltank.attack = random.randint(3,8)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_literaltank.attack = Federation_literaltank.attack * 2
            self.hp = self.hp - Federation_literaltank.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_literaltank.attack

    def ms_atk(self):
        MegaCorp_Soldier.attack = random.randint(8, 15)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_Soldier.attack = MegaCorp_Soldier.attack * 2
            self.hp = self.hp - MegaCorp_Soldier.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - MegaCorp_Soldier.attack

    def mm_atk(self):
        MegaCorp_Medic.attack = random.randint(2, 5)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_Medic.attack = MegaCorp_Medic.attack * 2
            self.hp = self.hp - MegaCorp_Medic.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - MegaCorp_Medic.attack

    def mt_atk(self):
        MegaCorp_literaltank.attack = random.randint(3, 8)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_literaltank.attack = MegaCorp_literaltank.attack * 2
            self.hp = self.hp - MegaCorp_literaltank.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - MegaCorp_literaltank.attack

    #boss stuff
    def fa_atk(self):
        Federation_Artillery_Unit.attack = random.randint(8, 15)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_Artillery_Unit.attack = Federation_Artillery_Unit.attack * 2
            self.hp = self.hp - Federation_Artillery_Unit.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_Artillery_Unit.attack

    def fcm_atk(self):
        Federation_Combat_Medic.attack = random.randint(8, 15)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_Combat_Medic.attack = Federation_Combat_Medic.attack * 2
            self.hp = self.hp - Federation_Combat_Medic.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_Combat_Medic.attack

    def fsd_atk(self):
        Federation_Space_Destroyer.attack = random.randint(8, 15)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_Space_Destroyer.attack = Federation_Space_Destroyer.attack * 2
            self.hp = self.hp - Federation_Space_Destroyer.attack
        else:
            if self.defensebull == True:
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_Space_Destroyer.attack

    def defend(self):
        defense = random.randint(1, 10)
        if defense >= 7:
            defensebull = False
        else:
            self.defensebull = True
Federation_Soldier = character("Federation Soldier", 100, random.randint(8,15), 100, False)
Federation_Medic = character("Federation Medic",45, random.randint(2,5), 45, False)
Federation_literaltank = character("Federation Tank",175, random.randint(3,8), 175, False)

MegaCorp_Soldier = character("Megacorp Soldier",100, random.randint(8,15), 100, False)
MegaCorp_Medic = character("Megacorp Medic",45, random.randint(2,5), 45, False)
MegaCorp_literaltank = character("Megacorp Tank",175, random.randint(3,8),175, False)
#bossfight stuff
Federation_Artillery_Unit = character("Federation Artillery Unit",70, random.randint(10,30), 200, False)
Federation_Combat_Medic = character("Federation Combat Medic",60, random.randint(5,8), 60, False)
Federation_Space_Destroyer = character("Federation Space Destroyer",350, random.randint(9,17), 350, False)

The_Star_of_Death = character("The Star of Death",500, random.randint(50,50), 500, False)

unit_list = [Federation_Soldier, Federation_Medic, Federation_literaltank, MegaCorp_Soldier, MegaCorp_Medic, MegaCorp_literaltank]
bossunitlist = [Federation_Artillery_Unit, Federation_Combat_Medic, Federation_Space_Destroyer, The_Star_of_Death]

character_selection()
while Federation_Medic.hp > 0 or Federation_literaltank.hp > 0 or Federation_Soldier.hp > 0:
    if MegaCorp_Soldier.hp > 0 or MegaCorp_Medic.hp > 0 or MegaCorp_literaltank.hp > 0:
        print("List of Character HP:")
        print(f"Federation Medic: {Federation_Medic.hp}")
        print(f"Federation Soldier: {Federation_Soldier.hp}")
        print(f"Federation Tank: {Federation_literaltank.hp}")
        print(f"Megacorp Medic: {MegaCorp_Medic.hp}")
        print(f"Megacorp Soldier: {MegaCorp_Soldier.hp}")
        print(f"Megacorp Tank: {MegaCorp_literaltank.hp}")
        character_selection()
    else:
        input("You have beat the enemy team! Would you like to play again (1), end the game (2), or go to the boss level? (3)")
        if input == "1":
            print("List of Character HP:")
            print(f"Federation Medic: {Federation_Medic.hp}")
            print(f"Federation Soldier: {Federation_Soldier.hp}")
            print(f"Federation Tank: {Federation_literaltank.hp}")
            print(f"Megacorp Medic: {MegaCorp_Medic.hp}")
            print(f"Megacorp Soldier: {MegaCorp_Soldier.hp}")
            print(f"Megacorp Tank: {MegaCorp_literaltank.hp}")
            character_selection()
        elif input == "2":
            print("Thank you for playing, and congrats on winning!")
            exit()
        elif input == "3":
            print("Your characters have been upgraded!")
else:
    Federation_Medic.hp <= 0 and Federation_literaltank.hp <= 0 and Federation_Soldier.hp <= 0
    input("Your entire team is dead! Play again? (Y/N)")
    if input == "Y" or input == "y":
        print("List of Character HP:")
        print(f"Federation Medic: {Federation_Medic.hp}")
        print(f"Federation Soldier: {Federation_Soldier.hp}")
        print(f"Federation Tank: {Federation_literaltank.hp}")
        print(f"Megacorp Medic: {MegaCorp_Medic.hp}")
        print(f"Megacorp Soldier: {MegaCorp_Soldier.hp}")
        print(f"Megacorp Tank: {MegaCorp_literaltank.hp}")
        character_selection()
    elif input == "N" or input == "n":
        print("Thank you for playing!")
        exit()

