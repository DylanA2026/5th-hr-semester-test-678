#Name:
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

#scrum document https://docs.google.com/document/d/1XU_0WKvlP_YzgnJlYu1qkNLJKQb57vK7oFyIBUQIiBI/edit?usp=sharing
import random
import time

from Hogan import choose_ally


class character:
    def __init__(self, hp, attack, maxhp, defensebull):
        self.hp = hp
        self.attack = attack
        self.maxhp = maxhp
        self.defensebull = defensebull
    def heal(self):
        self.hp = self.hp + random.randint(20, 30)
        if self.hp > self.maxhp:
            self.hp = self.maxhp


    def fsAtk(self):
        Federation_Soldier.attack = random.randint(8,15)
        crit = random.randint(1,20)
        if crit == 20:
            Federation_Soldier.attack = Federation_Soldier.attack * 2
            self.hp = self.hp - Federation_Soldier.attack
            print("Critical Attack")
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_Soldier.attack

    def fmAtk(self):
        Federation_Medic.attack = random.randint(2,5)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_Medic.attack = Federation_Medic.attack * 2
            self.hp = self.hp - Federation_Medic.attack
            print("Critical Attack")
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_Medic.attack

    def ftAtk(self):
        Federation_literaltank.attack = random.randint(3,8)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_literaltank.attack = Federation_literaltank.attack * 2
            self.hp = self.hp - Federation_literaltank.attack
            print("Critical Attack")
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
            else:
                self.hp = self.hp - Federation_literaltank.attack

    def msAtk(self):
        MegaCorp_Soldier.attack = random.randint(8, 15)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_Soldier.attack = MegaCorp_Soldier.attack * 2
            self.hp = self.hp - MegaCorp_Soldier.attack
            print("Critical Attack")
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
            else:
                self.hp = self.hp - MegaCorp_Soldier.attack

    def mmAtk(self):
        MegaCorp_Medic.attack = random.randint(2, 5)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_Medic.attack = MegaCorp_Medic.attack * 2
            self.hp = self.hp - MegaCorp_Medic.attack
            print("Critical Attack")
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
            else:
                self.hp = self.hp - MegaCorp_Medic.attack

    def mtAtk(self):
        MegaCorp_literaltank.attack = random.randint(3, 8)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_literaltank.attack = MegaCorp_literaltank.attack * 2
            self.hp = self.hp - MegaCorp_literaltank.attack
            print("Critical Attack")
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
            else:
                self.hp = self.hp - MegaCorp_literaltank.attack

    def defend(self):
        defense = random.randint(1, 10)
        if defense >= 7:
            print("Defense Failed!")
        else:
            self.defensebull = True
            print("Defense Successful! Character will be defended on the next attack")
Federation_Soldier = character(100, random.randint(8,15), 100, False)
Federation_Medic = character(45, random.randint(2,5), 45, False)
Federation_literaltank = character(175, random.randint(3,8), 175, False)

MegaCorp_Soldier = character(100, random.randint(8,15), 100, False)
MegaCorp_Medic = character(45, random.randint(2,5), 45, False)
MegaCorp_literaltank = character(175, random.randint(3,8),175, False)

unit_list = [Federation_Soldier, Federation_Medic, Federation_literaltank, MegaCorp_Soldier, MegaCorp_Medic, MegaCorp_literaltank]
char_select = 0
print("Welcome to Space Masters")

def char_change_prompt():
    cont = int(input("Press 1 to continue or press 2 to change your character: "))
    if cont == 1:
        gameplay()
    elif cont == 2:
        character_selection()
    else:
        print("Not a valid option")
        char_change_prompt()

def character_selection():
    print("Select a character from the Federation of Space Masters")
    global char_select
    char_select = int(input("Enter 1 to select Soldier, 2 to select Medic, and 3 to select Space Tank: "))
    if char_select == 1:
        print("You have selected the Space Soldier")
        char_change_prompt()

    elif char_select == 2:
        print("You have selected the Space Medic")
        char_change_prompt()

    elif char_select == 3:
        print("You have selected the Space Tank")
        char_change_prompt()
    else:
        print("Not a valid option")
        character_selection()



def gameplay():
    #Soldier Character
    if char_select == 1:
        choose_action = int(input("Enter 1 to attack or 2 to defend your character: "))
        if choose_action == 1:
            choose_enemy = int(input("Enter 1 to attack MegaCorp Soldier, 2 to attack MegaCorp Medic, or 3 to attack MegaCorp Tank"))
            #Fed Soldier attacking MC Soldier
            if choose_enemy == 1:
                MegaCorp_Soldier.fsAtk()
                # Fed Soldier attacking MC Medic
            elif choose_enemy == 2:
                MegaCorp_Medic.fsAtk()
                # Fed Soldier attacking MC Tank
            elif choose_enemy == 3:
                MegaCorp_literaltank.fsAtk()
            else:
                print("Not a valid option")
                gameplay()

        elif choose_action == 2:
            print("You have chosen to defend your character")
            Federation_Soldier.defend()
            time.sleep(0.4)
        else:
            print("Not a valid option")
            gameplay()

# Medic Character
    elif char_select == 2:
        choose_action = int(input("Enter 1 to attack, 2 to defend your character, or 3 to heal a character: "))
        if choose_action == 1:
            choose_enemy = int(input("Enter 1 to attack MegaCorp Soldier, 2 to attack MegaCorp Medic, or 3 to attack MegaCorp Tank"))
            # Fed Medic attacking MC Soldier
            if choose_enemy == 1:
                MegaCorp_Soldier.fmAtk()
                # Fed Medic attacking MC Medic
            elif choose_enemy == 2:
                MegaCorp_Medic.fmAtk()
                # Fed Medic attacking MC Tank
            elif choose_enemy == 3:
                MegaCorp_literaltank.fmAtk()
            else:
                print("Not a valid option")
                gameplay()

        elif choose_action == 2:
            print("You have chosen to defend your character")
            Federation_Medic.defend()
        elif choose_action == 3:
            print("You have chosen to heal a character")
            choose_enemy = int(input("Enter 1 to heal Federation Solider or 2 to heal Federation Tank"))
            # Fed Medic attacking MC Soldier
            if choose_enemy == 1:
                Federation_Soldier.heal()
                # Fed Medic attacking MC Medic
            elif choose_enemy == 2:
                Federation_literaltank.heal()
            else:
                print("Not a valid option")
                gameplay()

        else:
            print("Not a valid option")
            gameplay()

#Tank Character
    elif char_select == 3:
        print("You have selected the Space Tank")
        choose_action = int(input("Enter 1 to attack or 2 to defend your character: "))
        if choose_action == 1:
            choose_enemy = int(
                input("Enter 1 to attack MegaCorp Soldier, 2 to attack MegaCorp Medic, or 3 to attack MegaCorp Tank"))
            #Fed Tank attacking MC Soldier
            if choose_enemy == 1:
                MegaCorp_Soldier.ftAtk()
                # Fed Tank attacking MC Medic
            elif choose_enemy == 2:
                MegaCorp_Medic.ftAtk()
                # Fed Tank attacking MC Tank
            elif choose_enemy == 3:
                MegaCorp_literaltank.ftAtk()
            else:
                print("Not a valid option")
                gameplay()

        elif choose_action == 2:
            print("You have chosen to defend your character")
            Federation_literaltank.defend()

        else:
            print("Not a valid option")
            gameplay()
    else:
        print("Character not selected, try again")
        character_selection()


def enemyatk():
    choose_ally = random.randint(1,3)
    if choose_ally == 1:
        Federation_Soldier.msAtk()
    elif choose_ally == 2:
        Federation_Medic.mmAtk()
    elif choose_ally == 3:
        Federation_literaltank.mtAtk()




character_selection()