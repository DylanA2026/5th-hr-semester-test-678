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
import time


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


    def fs_atk(self):
        Federation_Soldier.attack = random.randint(8,15)
        crit = random.randint(1,20)
        if crit == 20:
            Federation_Soldier.attack = Federation_Soldier.attack * 2
            self.hp = self.hp - Federation_Soldier.attack
        else:
            if self.defensebull == True:
                print("The Federation Soldier is defended!")
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
                print("The Federation Medic is defended!")
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
                print("The Federation Tank is defended!")
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
                print("The Megacorp Soldier is defended!")
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
            self.hp = self.hp - MegaCorp_Medic.attack

    def mt_atk(self):
        MegaCorp_literaltank.attack = random.randint(3, 8)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_literaltank.attack = MegaCorp_literaltank.attack * 2
            self.hp = self.hp - MegaCorp_literaltank.attack
        else:
            self.hp = self.hp - MegaCorp_literaltank.attack

    def defend(self):
        defense = random.randint(1, 10)
        if defense >= 7:
            print("Defense Failed!")
        else:
            self.defensebull = True
Federation_Soldier = character(100, random.randint(8,15), 100, False)
Federation_Medic = character(45, random.randint(2,5), 45, False)
Federation_literaltank = character(175, random.randint(3,8), 175, False)

MegaCorp_Soldier = character(100, random.randint(8,15), 100, False)
MegaCorp_Medic = character(45, random.randint(2,5), 45, False)
MegaCorp_literaltank = character(175, random.randint(3,8),175, False)