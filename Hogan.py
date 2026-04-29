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


import random

def intro():
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXX")
    print("XXXXXXXXXXXX")
    print("XXXXXXXXXXX")
    print("XXXXXXXXXX")
    print("XXXXXXXXX")
    print("XXXXXXXX")
    print("XXXXXXX")
    print("XXXXXX")
    print("XXXXX")
    print("XXXX")
    print("XXX")
    print("XX")
    print("X")
    print("XX")
    print("XXX")
    print("XXXX")
    print("XXXXX")
    print("XXXXXX")
    print("XXXXXXX")
    print("XXXXXXXX")
    print("XXXXXXXXX")
    print("XXXXXXXXXX")
    print("XXXXXXXXXXX")
    print("XXXXXXXXXXXX")
    print("XXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXXXX")
    print("XXXXXXXXXXXXXXXXXXXXXXXXX")


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
    # Fed Soldier attacking MC Tank
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


unit_list = [Federation_Soldier, Federation_Medic, Federation_literaltank, MegaCorp_Soldier, MegaCorp_Medic, MegaCorp_literaltank]

character_selection()
while Federation_Medic.hp > 0 or Federation_literaltank.hp > 0 or Federation_Soldier.hp > 0:
    if MegaCorp_Soldier.hp > 0 or MegaCorp_Medic.hp > 0 or MegaCorp_literaltank.hp > 0:
        character_selection()
    else:
        input("You have beat the enemy team! Play again? (Y/N)")
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
            print("Thank you for playing, and congrats on winning!")
            exit()
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

