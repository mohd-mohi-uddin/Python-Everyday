import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
memory = []
# TODO-1: - Use a while loop to let the user guess again.
while True:
    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            memory.append(guess)
        elif letter in memory:
            display += letter
        else:
            display += "_"

    print(display)
 
    if "_" not in display:
        print("you win")
        break