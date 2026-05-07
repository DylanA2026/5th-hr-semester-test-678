import random
import time
#WARNING: THE BOSSFIGHT IS NOT LIKELY TO EVER BE FINISHED.
bosslevel = False
level = True
class character:
    def __init__(self, name, hp, attack, maxhp, defensebull):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.maxhp = maxhp
        self.defensebull = defensebull

    def healfriendly(self):
        self.hp = self.hp + random.randint(20, 30)
        if self.hp <= 0:
            print("You cannot heal a dead player!")
            gameplay()
        else:
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            print(f"{self.name} has been healed to {self.hp} hp.")
            time.sleep(0.6)
    def healenemy(self):
        self.hp = self.hp + random.randint(10, 25)
        if self.hp <= 0:
            enemyatk()
        else:
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            print(f"{self.name} has been healed to {self.hp} hp.")
            time.sleep(0.6)


    def fsAtk(self):
        if self.hp <= 0:
            print("Player is already dead! Attack another character!")
            gameplay()


        Federation_Soldier.attack = random.randint(8,15)
        crit = random.randint(1,20)
        if crit == 20:
            Federation_Soldier.attack = Federation_Soldier.attack * 2
            self.hp = self.hp - Federation_Soldier.attack
            print("Critical Attack")
            print(f"Federation Soldier has hit {self.name} for {Federation_Soldier.attack} Damage")
            print(f"{self.name} has {self.hp} hp remaining.")
            time.sleep(0.6)
            enemyatk()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                time.sleep(0.6)
                enemyatk()
            else:
                self.hp = self.hp - Federation_Soldier.attack
                print(f"Federation Soldier has hit {self.name} for {Federation_Soldier.attack} Damage")
                print(f"{self.name} has {self.hp} hp remaining.")
                time.sleep(0.6)
                enemyatk()

    def fmAtk(self):
        if self.hp <= 0:
            print("Player is already dead! Attack another character!")
            gameplay()
        Federation_Medic.attack = random.randint(2,5)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_Medic.attack = Federation_Medic.attack * 2
            self.hp = self.hp - Federation_Medic.attack
            print("Critical Attack")
            print(f"Federation Medic has hit {self.name} for {Federation_Medic.attack} Damage")
            print(f"{self.name} has {self.hp} hp remaining.")
            time.sleep(0.6)
            enemyatk()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                time.sleep(0.6)
                enemyatk()
            else:
                self.hp = self.hp - Federation_Medic.attack
                print(f"Federation Medic has hit {self.name} for {Federation_Medic.attack} Damage")
                print(f"{self.name} has {self.hp} hp remaining.")
                time.sleep(0.6)
                enemyatk()

    def ftAtk(self):
        if self.hp <= 0:
            print("Player is already dead! Attack another character!")
            gameplay()
        Federation_literaltank.attack = random.randint(3,8)
        crit = random.randint(1, 20)
        if crit == 20:
            Federation_literaltank.attack = Federation_literaltank.attack * 2
            self.hp = self.hp - Federation_literaltank.attack
            print("Critical Attack")
            print(f"Federation Tank has hit {self.name} for {Federation_literaltank.attack} Damage")
            print(f"{self.name} has {self.hp} hp remaining.")
            time.sleep(0.6)
            enemyatk()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                time.sleep(0.6)
                enemyatk()
            else:
                self.hp = self.hp - Federation_literaltank.attack
                print(f"Federation Tank has hit {self.name} for {Federation_literaltank.attack} Damage")
                print(f"{self.name} has {self.hp} hp remaining.")
                time.sleep(0.6)
                enemyatk()

    def msAtk(self):
        if self.hp <= 0 or MegaCorp_Soldier.hp <= 0:
            if self.hp <= 0:
                print("Player is already dead! Attack another character!")
                enemyatk()
            else:
                print("MegaCorp Soldier is dead! They cannot attack")
                enemyatk()
        MegaCorp_Soldier.attack = random.randint(8, 15)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_Soldier.attack = MegaCorp_Soldier.attack * 2
            self.hp = self.hp - MegaCorp_Soldier.attack
            print("Critical Attack")
            print(f"MegaCorp Soldier has hit {self.name} for {MegaCorp_Soldier.attack} Damage")
            print(f"{self.name} has {self.hp} hp remaining.")
            time.sleep(0.6)
            start_game()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                time.sleep(0.6)
                start_game()
            else:
                self.hp = self.hp - MegaCorp_Soldier.attack
                print(f"MegaCorp Soldier has hit {self.name} for {MegaCorp_Soldier.attack} Damage")
                print(f"{self.name} has {self.hp} hp remaining.")
                time.sleep(0.6)
                start_game()

    def mmAtk(self):
        if self.hp <= 0 or MegaCorp_Medic.hp <= 0:
            if self.hp <= 0:
                print("Player is already dead! Attack another character!")
                enemyatk()
            else:
                print("MegaCorp Medic is Dead! They cannot attack")
                enemyatk()
        MegaCorp_Medic.attack = random.randint(2, 5)
        crit = random.randint(1, 20)
        if crit == 20:
            MegaCorp_Medic.attack = MegaCorp_Medic.attack * 2
            self.hp = self.hp - MegaCorp_Medic.attack
            print("Critical Attack")
            print(f"MegaCorp Medic has hit {self.name} for {MegaCorp_Medic.attack} Damage")
            print(f"{self.name} has {self.hp} hp remaining.")
            time.sleep(0.6)
            start_game()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                time.sleep(0.6)
                start_game()
            else:
                self.hp = self.hp - MegaCorp_Medic.attack
                print(f"MegaCorp Medic has hit {self.name} for {MegaCorp_Medic.attack} Damage")
                print(f"{self.name} has {self.hp} hp remaining.")
                time.sleep(0.6)
                start_game()

    def mtAtk(self):
        if self.hp <= 0 or MegaCorp_literaltank.hp <= 0:
            if self.hp <= 0:
                print("Player is already dead! Attack another character!")
                enemyatk()
            else:
                print("MegaCorp Tank is disabled! They cannot attack")
                enemyatk()
        MegaCorp_literaltank.attack = random.randint(3, 8)
        crit = random.randint(1, 20)

        if crit == 20:
            MegaCorp_literaltank.attack = MegaCorp_literaltank.attack * 2
            self.hp = self.hp - MegaCorp_literaltank.attack
            print("Critical Attack")
            print(f"MegaCorp Tank has hit {self.name} for {MegaCorp_literaltank.attack} Damage")
            print(f"{self.name} has {self.hp} hp remaining.")
            time.sleep(0.6)
            start_game()
        else:
            if self.defensebull == True:
                print("The attack was blocked!")
                self.defensebull = False
                time.sleep(0.6)
                start_game()
            else:
                self.hp = self.hp - MegaCorp_literaltank.attack
                print(f"MegaCorp Tank has hit {self.name} for {MegaCorp_literaltank.attack} Damage")
                print(f"{self.name} has {self.hp} hp remaining.")
                time.sleep(0.6)
                start_game()
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
            print("Defense Failed!")
            time.sleep(0.6)
        else:
            self.defensebull = True
            print("Defense Successful! Character will be defended on the next attack")
            time.sleep(0.6)

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
    print("1. Soldier\n2. Medic\n3. Space Tank")
    char_select = int(input("Enter choice: (1-3) "))
    if char_select == 1:
        if Federation_Soldier.hp <= 0:
            print("This character has no hp remaining.! \n Select a new character:")
            character_selection()
        print("You have selected the Space Soldier")
        char_change_prompt()

    elif char_select == 2:
        if Federation_Medic.hp <= 0:
            print("This character has no hp remaining.! \n Select a new character:")
            character_selection()
        print("You have selected the Space Medic")
        char_change_prompt()

    elif char_select == 3:
        if Federation_literaltank.hp <= 0:
            print("This character has no hp remaining.! \n Select a new character:")
            character_selection()
        print("You have selected the Space Tank")
        char_change_prompt()

    elif char_select == 64:
        boss_character_selection()
    else:
        print("Not a valid option")
        character_selection()



def gameplay():
    #Soldier Character
    if char_select == 1:
        print("1. Attack\n2. Defend:")
        choose_action = int(input("Enter Choice: "))
        if choose_action == 1:
            print("1. Attack MegaCorp Soldier\n2. Attack MegaCorp Medic\n3. Attack MegaCorp Space Tank")
            choose_enemy = int(input("Enter Choice: (1-3)"))
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
            time.sleep(0.6)
            enemyatk()
        else:
            print("Not a valid option")
            gameplay()

# Medic Character
    elif char_select == 2:
        print("1. Attack\n2. Defend\n3. Heal a character:")
        choose_action = int(input("Enter Choice: "))
        if choose_action == 1:
            choose_enemy = int(input("Enter 1. Attack MegaCorp Soldier\n2. Attack MegaCorp Medic\n3. Attack MegaCorp Space Tank"))
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
                Federation_Soldier.healfriendly()
                enemyatk()
                # Fed Medic attacking MC Medic
            elif choose_enemy == 2:
                Federation_literaltank.healfriendly()
                enemyatk()
            else:
                print("Not a valid option")
                gameplay()

        else:
            print("Not a valid option")
            gameplay()

#Tank Character
    elif char_select == 3:
        print("1. Attack\n2. Defend:")
        choose_action = int(input("Enter Choice: "))
        if choose_action == 1:
            choose_enemy = int(
                input("Enter 1. Attack MegaCorp Soldier\n2. Attack MegaCorp Medic\n3. Attack MegaCorp Space Tank"))
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
    action = random.randint(1, 4)
    while action == 1 or action == 2 or action == 3:
        if enemy == 1:
            if action == 1 or action == 2:
                if ally == 1:
                    Federation_Soldier.msAtk()
                elif ally == 2:
                    Federation_Medic.msAtk()
                elif ally == 3:
                    Federation_literaltank.msAtk()
            elif action == 3:
                print("enemy has chosen to defend their character")
                MegaCorp_Soldier.defend()
                time.sleep(0.6)
                start_game()


        elif enemy == 2:
            if action == 1 or action == 2:
                if ally == 1:
                    Federation_Soldier.mmAtk()
                elif ally == 2:
                    Federation_Medic.mmAtk()
                elif ally == 3:
                    Federation_literaltank.mmAtk()
            elif action == 3:
                print("enemy has chosen to defend their character")
                MegaCorp_Medic.defend()
                time.sleep(0.6)
                start_game()

        elif enemy == 3:
            if action == 1 or action == 2:
                if ally == 1:
                    Federation_Soldier.mtAtk()
                elif ally == 2:
                    Federation_Medic.mtAtk()
                elif ally == 3:
                    Federation_literaltank.mtAtk()
            elif action == 3:
                print("enemy has chosen to defend their character")
                MegaCorp_literaltank.defend()
                time.sleep(0.6)
                start_game()
    else:
        if action == 4:
            enemy_heal = random.randint(1,2)
            if enemy_heal == 1:
                MegaCorp_Soldier.healenemy()
                start_game()
            else:
                MegaCorp_literaltank.healenemy()
                start_game()

#Boss stuff

def boss_gameplay():
    #Soldier Character
    if char_select == 1:
        print("1. Attack\n2. Defend:")
        choose_action = int(input("Enter Choice: "))
        if choose_action == 1:
            print("Attack MegaCorp Star of Death? (Y/N")
            choose_enemy = int(input("Enter Choice:"))
            #Fed Soldier attacking MC Soldier
            if choose_enemy == "Y" or "y":
                The_Star_of_Death.fa_Atk()
                # Fed Soldier attacking MC Medic
            elif choose_enemy == "N" or "n":
                boss_gameplay()
            else:
                print("Not a valid option")
                boss_gameplay()

        elif choose_action == 2:
            print("You have chosen to defend your character")
            Federation_Artillery_Unit.defend()
            time.sleep(0.6)
            enemyatk()
        else:
            print("Not a valid option")
            gameplay()

    elif char_select == 2:
        print("1. Attack\n2. Defend\n3. Heal a character:")
        choose_action = int(input("Enter Choice: "))
        if choose_action == 1:
            print("Attack MegaCorp Star of Death? (Y/N")
            choose_enemy = int(input("Enter Choice:"))
            # Fed Soldier attacking MC Soldier
            if choose_enemy == "Y" or "y":
                The_Star_of_Death.fcm_atk()
                # Fed Soldier attacking MC Medic
            elif choose_enemy == "N" or "n":
                boss_gameplay()
            else:
                print("Not a valid option")
                boss_gameplay()

        elif choose_action == 2:
            print("You have chosen to defend your character")
            Federation_Combat_Medic.defend()
            time.sleep(0.6)
            enemyatk()
        elif choose_action == 3:
            print("You have chosen to heal a character")
            choose_enemy = int(input("Enter 1 to heal Federation Artillery or 2 to repair Federation Destroyer"))
            # Fed Medic attacking MC Soldier
            if choose_enemy == 1:
                Federation_Artillery_Unit.healfriendly()
                boss_enemyatk()
                # Fed Medic attacking MC Medic
            elif choose_enemy == 2:
                Federation_Space_Destroyer.healfriendly()
                boss_enemyatk()
            else:
                print("Not a valid option")
                gameplay()

        else:
            print("Not a valid option")
            gameplay()

    # Tank Character
    elif char_select == 3:
        print("1. Attack\n2. Defend:")
        choose_action = int(input("Enter Choice: "))
        if choose_action == 1:
            choose_enemy = int(
                input("Enter 1. Attack MegaCorp Soldier\n2. Attack MegaCorp Medic\n3. Attack MegaCorp Space Tank"))
            # Fed Tank attacking MC Soldier
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

Federation_Artillery_Unit = character("Federation Artillery Unit",70, random.randint(10,45), 200, False)
Federation_Combat_Medic = character("Federation Combat Medic",60, random.randint(5,10), 60, False)
Federation_Space_Destroyer = character("Federation Space Destroyer",350, random.randint(10,20), 350, False)

The_Star_of_Death = character("The Star of Death",500, random.randint(50,50), 500, False)

def boss_char_change_prompt():
    cont = int(input("Press 1 to continue or press 2 to change your character: "))
    if cont == 1:
        boss_gameplay()
    elif cont == 2:
        boss_character_selection()
    else:
        print("Not a valid option")
        boss_char_change_prompt()

def boss_character_selection():
    print("Select an upgraded character from the Federation of Space Masters")
    global char_select
    print("1. Artillery Unit\n2. Combat Medic\n3. Space Destroyer")
    char_select = int(input("Enter choice: (1-3) "))
    if char_select == 1:
        print("You have selected the Artillery unit")
        boss_char_change_prompt()

    elif char_select == 2:
        print("You have selected the Combat Medic")
        boss_char_change_prompt()

    elif char_select == 3:
        print("You have selected the Space Destroyer")
        boss_char_change_prompt()
    else:
        print("Not a valid option")
        boss_character_selection()

bossunitlist = [Federation_Artillery_Unit, Federation_Combat_Medic, Federation_Space_Destroyer]

def start_game():
    global level
    global bosslevel
    if level == True:
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
                input(
                    "You have beat the enemy team! Would you like to play again (1), end the game (2), or go to the boss level? (3)")
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
                    print(f"Your new Characters:{bossunitlist}")
                    bosslevel = True
                    level = False
                    boss_character_selection()
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
    else:
        while Federation_Combat_Medic.hp > 0 or Federation_Space_Destroyer.hp > 0 or Federation_Artillery_Unit.hp > 0:
            if The_Star_of_Death.hp > 0:
                boss_character_selection()
                print("List of Character HP:")
                print(f"Federation Combat Medic: {Federation_Combat_Medic.hp}")
                print(f"Federation Artillery: {Federation_Artillery_Unit.hp}")
                print(f"Federation Space Destroyer: {Federation_Space_Destroyer.hp}")
                print(f"The Megacorp Star of Death: {The_Star_of_Death.hp}")
            else:
                input(
                    "You have beat the enemy team! Would you like to play again (1), end the game (2), or go to the first level? (3)")
                if input == "1":
                    print("List of Character HP:")
                    print(f"Federation Medic: {Federation_Medic.hp}")
                    print(f"Federation Soldier: {Federation_Soldier.hp}")
                    print(f"Federation Tank: {Federation_literaltank.hp}")
                    print(f"Megacorp Medic: {MegaCorp_Medic.hp}")
                    print(f"Megacorp Soldier: {MegaCorp_Soldier.hp}")
                    print(f"Megacorp Tank: {MegaCorp_literaltank.hp}")
                    boss_character_selection()
                elif input == "2":
                    print("Thank you for playing, and congrats on winning!")
                    exit()
                elif input == "3":
                    print("Your characters have been downgraded!")
                    print(f"Your new Characters:{bossunitlist}")
                    bosslevel = False
                    level = True
                    boss_character_selection()
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
# Install required library: pip install art
from art import tprint

# Bold and Large Text
print("\033[1m")  # Start Bold
tprint("Space Masters")
print("\033[0m")  # Reset Style

time.sleep(0.4)
start_game()