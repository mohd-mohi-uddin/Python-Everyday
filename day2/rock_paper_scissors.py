import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    choice = int(input('what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n'))
    if choice ==  0:
        print(rock)
        break
    elif choice == 1:
        print(paper)
        break
    elif choice == 2:
        print(scissors)
        break
    else:
        print("'type error', Type 0 for Rock, 1 for Paper, 2 for Scissors.")

print('\nComputer chooses:')
computer_choice = random.choice([rock,paper,scissors])
print(computer_choice)

if choice == 0 and computer_choice == rock:
    print('its a draw')
if choice == 0 and computer_choice == paper:
    print('computer wins')
if choice == 0 and computer_choice == scissors:
    print('you win')
if choice == 1 and computer_choice == paper:
    print('its a draw')
if choice == 1 and computer_choice == scissors:
    print('computer wins')
if choice == 1 and computer_choice == rock:
    print('you win')
if choice == 2 and computer_choice == scissors:
    print('its a draw')
if choice == 2 and computer_choice == rock:
    print('computer wins')
if choice == 2 and computer_choice == paper:
    print('you win')
