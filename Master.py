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
            print(f"{self.name} has been healed to {self.hp} hp.")


    def fsAtk(self):
        Federation_Soldier.attack = random.randint(8,15)
        crit = random.randint(1,20)
        if crit == 20:
            Federation_Soldier.attack = Federation_Soldier.attack * 2
            self.hp = self.hp - Federation_Soldier.attack
            print("Critical Attack")
            print(f"Federation Soldier has hit {self.name} for {Federation_Soldier.attack} Damage")
            enemyatk()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                enemyatk()
            else:
                self.hp = self.hp - Federation_Soldier.attack
                print(f"Federation Soldier has hit {self.name} for {Federation_Soldier.attack} Damage")
                enemyatk()

    def fmAtk(self):
        Federation_Medic.attack = random.randint(2,5)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_Medic.attack = Federation_Medic.attack * 2
            self.hp = self.hp - Federation_Medic.attack
            print("Critical Attack")
            print(f"Federation Medic has hit {self.name} for {Federation_Medic.attack} Damage")
            enemyatk()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                enemyatk()
            else:
                self.hp = self.hp - Federation_Medic.attack
                print(f"Federation Medic has hit {self.name} for {Federation_Medic.attack} Damage")
                enemyatk()

    def ftAtk(self):
        Federation_literaltank.attack = random.randint(3,8)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_literaltank.attack = Federation_literaltank.attack * 2
            self.hp = self.hp - Federation_literaltank.attack
            print("Critical Attack")
            print(f"Federation Tank has hit {self.name} for {Federation_literaltank.attack} Damage")
            enemyatk()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                enemyatk()
            else:
                self.hp = self.hp - Federation_literaltank.attack
                print(f"Federation Tank has hit {self.name} for {Federation_literaltank.attack} Damage")
                enemyatk()

    def msAtk(self):
        MegaCorp_Soldier.attack = random.randint(8, 15)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_Soldier.attack = MegaCorp_Soldier.attack * 2
            self.hp = self.hp - MegaCorp_Soldier.attack
            print("Critical Attack")
            print(f"MegaCorp Soldier has hit {self.name} for {MegaCorp_Soldier.attack} Damage")
            start_game()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                start_game()
            else:
                self.hp = self.hp - MegaCorp_Soldier.attack
                print(f"MegaCorp Soldier has hit {self.name} for {MegaCorp_Soldier.attack} Damage")
                start_game()

    def mmAtk(self):
        MegaCorp_Medic.attack = random.randint(2, 5)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_Medic.attack = MegaCorp_Medic.attack * 2
            self.hp = self.hp - MegaCorp_Medic.attack
            print("Critical Attack")
            print(f"MegaCorp Medic has hit {self.name} for {MegaCorp_Medic.attack} Damage")
            start_game()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                start_game()
            else:
                self.hp = self.hp - MegaCorp_Medic.attack
                print(f"MegaCorp Medic has hit {self.name} for {MegaCorp_Medic.attack} Damage")
                start_game()

    def mtAtk(self):
        MegaCorp_literaltank.attack = random.randint(3, 8)
        crit = random.randint(1, 20)

        if crit == 20:
            MegaCorp_literaltank.attack = MegaCorp_literaltank.attack * 2
            self.hp = self.hp - MegaCorp_literaltank.attack
            print("Critical Attack")
            print(f"MegaCorp Tank has hit {self.name} for {MegaCorp_literaltank.attack} Damage")
            start_game()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                start_game()
            else:
                self.hp = self.hp - MegaCorp_literaltank.attack
                print(f"MegaCorp Tank has hit {self.name} for {MegaCorp_literaltank.attack} Damage")
                start_game()

    def defend(self):
        defense = random.randint(1, 10)
        if defense >= 7:
            print("Defense Failed!")
        else:
            self.defensebull = True
            print("Defense Successful! Character will be defended on the next attack")

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
            enemyatk()
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
            enemyatk()
        elif choose_action == 3:
            print("You have chosen to heal a character")
            choose_enemy = int(input("Enter 1 to heal Federation Solider or 2 to repair Federation Tank"))
            # Fed Medic attacking MC Soldier
            if choose_enemy == 1:
                Federation_Soldier.heal()
                enemyatk()
                # Fed Medic attacking MC Medic
            elif choose_enemy == 2:
                Federation_literaltank.heal()
                enemyatk()
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
            enemyatk()

        else:
            print("Not a valid option")
            gameplay()
    else:
        print("Character not selected, try again")
        character_selection()


def enemyatk():
    enemy = random.randint(1,3)
    ally = random.randint(1, 3)
    action = random.randint(1, 3)
    while action == 1 or action == 2:
        if enemy == 1:
            if action == 1:
                if ally == 1:
                    Federation_Soldier.msAtk()
                elif ally == 2:
                    Federation_Medic.msAtk()
                elif ally == 3:
                    Federation_literaltank.msAtk()
            elif action == 2:
                    print("enemy has chosen to defend their character")
                    MegaCorp_Soldier.defend()

        elif enemy == 2:
            if action == 1:
                if ally == 1:
                    Federation_Soldier.mmAtk()
                elif ally == 2:
                    Federation_Medic.mmAtk()
                elif ally == 3:
                    Federation_literaltank.mmAtk()
            elif action == 2:
                print("enemy has chosen to defend their character")
                MegaCorp_Medic.defend()

        elif enemy == 3:
            if action == 1:
                if ally == 1:
                    Federation_Soldier.mtAtk()
                elif ally == 2:
                    Federation_Medic.mtAtk()
                elif ally == 3:
                    Federation_literaltank.mtAtk()
            elif action == 2:
                print("enemy has chosen to defend their character")
                MegaCorp_literaltank.defend()
    else:
        if action == 3:
            enemy_heal = random.randint(1,3)
            if enemy_heal == 1:
                MegaCorp_Soldier.heal()
                start_game()
            elif enemy_heal == 2:
                MegaCorp_Medic.heal()
                start_game()
            else:
                MegaCorp_literaltank.heal()
                start_game()






def start_game():
    while Federation_Medic.hp > 0 or Federation_literaltank.hp > 0 or Federation_Soldier.hp > 0:
        if MegaCorp_Soldier.hp > 0 or MegaCorp_Medic.hp > 0 or MegaCorp_literaltank.hp > 0:
            character_selection()
            print("List of Character HP:")
            print(f"Federation Medic: {Federation_Medic.hp}")
            print(f"Federation Soldier: {Federation_Soldier.hp}")
            print(f"Federation Tank: {Federation_literaltank.hp}")
            print(f"Megacorp Medic: {MegaCorp_Medic.hp}")
            print(f"Megacorp Soldier: {MegaCorp_Soldier.hp}")
            print(f"Megacorp Tank: {MegaCorp_literaltank.hp}")
        else:

            playAgain = input("You have beat the enemy team! Play again? (Y/N)")

            if playAgain == "Y" or playAgain == "y":
                print("List of Character HP:")
                print(f"Federation Medic: {Federation_Medic.hp}")
                print(f"Federation Soldier: {Federation_Soldier.hp}")
                print(f"Federation Tank: {Federation_literaltank.hp}")
                print(f"Megacorp Medic: {MegaCorp_Medic.hp}")
                print(f"Megacorp Soldier: {MegaCorp_Soldier.hp}")
                print(f"Megacorp Tank: {MegaCorp_literaltank.hp}")
                character_selection()
            elif playAgain == "N" or playAgain == "n":
                print("Thank you for playing, and congrats on winning!")
                exit()
            else:
                print("Not a valid option")
    else:
        if Federation_Medic.hp <= 0 and Federation_literaltank.hp <= 0 and Federation_Soldier.hp <= 0:

            playAgain = input("You have lost to the enemy team! Play again? (Y/N)")

            if playAgain == "Y" or playAgain == "y":
                print("List of Character HP:")
                print(f"Federation Medic: {Federation_Medic.hp}")
                print(f"Federation Soldier: {Federation_Soldier.hp}")
                print(f"Federation Tank: {Federation_literaltank.hp}")
                print(f"Megacorp Medic: {MegaCorp_Medic.hp}")
                print(f"Megacorp Soldier: {MegaCorp_Soldier.hp}")
                print(f"Megacorp Tank: {MegaCorp_literaltank.hp}")
                character_selection()
            elif playAgain == "N" or playAgain == "n":
                print("Thank you for playing!")
                exit()
            else:
                print("Not a valid option")
        else:
            print("Not a valid option")

Federation_Soldier = character("Federation Soldier", 100, random.randint(8,15), 100, False)
Federation_Medic = character("Federation Medic",45, random.randint(2,5), 45, False)
Federation_literaltank = character("Federation Tank",175, random.randint(3,8), 175, False)

MegaCorp_Soldier = character("Megacorp Soldier",100, random.randint(8,15), 100, False)
MegaCorp_Medic = character("Megacorp Medic",45, random.randint(2,5), 45, False)
MegaCorp_literaltank = character("Megacorp Tank",175, random.randint(3,8),175, False)

unit_list = [Federation_Soldier, Federation_Medic, Federation_literaltank, MegaCorp_Soldier, MegaCorp_Medic, MegaCorp_literaltank]
char_select = 0
global playAgain
print("Welcome to Space Masters")

start_game()