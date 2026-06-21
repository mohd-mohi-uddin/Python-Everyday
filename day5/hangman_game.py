import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["chocolate","icecream","pizza","burger","frenchfries"]
choice = random.choice(word_list)
print(choice)

blanks = ""

for i in range(len(choice)):
    blanks += "_"
print(blanks)

gameover = False

memory = []

lives = 6

while not gameover:
    
    guess = input("choose a letter:")

    answer_to_show = ""

    for i in choice:
        if i == guess:
           answer_to_show += guess
           memory.append(guess)
           
        elif i in memory:
            answer_to_show += i

        else:
           answer_to_show += "_"
    print(answer_to_show)

    if guess not in choice:
        lives -= 1

        if lives == 0:
            gameover = True
            print("game over, you lose")

    print(stages[lives])

    if "_" not in answer_to_show:
        gameover = True
        print("gamr over, u won")

    