print('''
    *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[asim]
*******************************************************************************
''')
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.\n")
way = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if way == "right":
    crossing_lake = input('Do u want to swin to cross the lake or will u wait till the boat arrives, select "swin" or "wait"\n').lower()
    if crossing_lake == "wait":
        door = input('You crossed the lake. Now u have three doors to enter: RED, BLUE AND YELLOW. Which one you are going to choose?\n').lower()
        if door == "red":
            print('you win!')
        elif door == "blue":
            print('you lost, there was a tiger inside.')
        elif door == "yellow":
            print("you lost. there was a lion inside")
        else:
            print("type error. select the right option.")
    else:
        print("Game Over. u got eaten by the crocodiles.")
else:
    print("Fall into a hole. Game Over.")