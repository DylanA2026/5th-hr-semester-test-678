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
    char_select = int(input("Enter 1 to select Soldier, 2 to select Medic, and 3 to select Space Tank: "))

    if char_select == 1:
        print("You have selected the Space Soldier")
        cont = int(input("Press 1 to continue or press 2 to change your character: "))
        char_change_prompt()

    elif char_select == 2:
        print("You have selected the Space Medic")
        cont = int(input("Press 1 to continue or press 2 to change your character: "))
        char_change_prompt()

    elif char_select == 3:
        print("You have selected the Space Tank")
        cont = int(input("Press 1 to continue or press 2 to change your character: "))
        char_change_prompt()
    else:
        print("Not a valid option")
        character_selection()



def gameplay():
    print("Still in development")





character_selection()