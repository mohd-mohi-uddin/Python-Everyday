import random
logo = '''
                                                                                           
 _____ _____ _____ _____ _____    _____ _____ _____    _____ _____ _____ _____ _____ _____ 
|   __|  |  |   __|   __|   __|  |_   _|  |  |   __|  |   | |  |  |     | __  |   __| __  |
|  |  |  |  |   __|__   |__   |    | | |     |   __|  | | | |  |  | | | | __ -|   __|    -|
|_____|_____|_____|_____|_____|    |_| |__|__|_____|  |_|___|_____|_|_|_|_____|_____|__|__|
                                                                                                                                                                                              
'''
print(logo)

print("welcome to the number guessing game!".title())
print("iam thinking of a number between 1 and 100.".title())

numbers = list(range(1, 101))
choice = random.choice(numbers)

while True:

    hardness = input("\nchoose a difficulty level. type 'easy', 'medium' and 'hard':".title()).lower()

    if hardness == "hard":
        lives = 5
        print("\nyou have total 5 attempts".title())
        break
    if hardness == "medium":
        lives = 7
        print("\nyou have total 7 attempts".title())
        break
    elif hardness == "easy":
        lives = 10
        print("you have total 10 attempts".title())
        break
    else:
        print("typing error. type again:".title())
        

while True:

    if lives == 0:
        print(f"out of lives, restart the game.\nthe number was {choice}".title())
        break
    else:

        guess = int(input("\nmake a guess:".title()))

        if guess < choice:
            print("too low.\nguess again:".title())
            lives -= 1
            print(f"\n{lives} lives left!".title())
        

        elif guess > choice:
            print("too high.\nguess again:".title())
            lives -= 1
            print(f"\n{lives} lives left!".title())
            

        elif guess == choice:
            print("\nAmazing! YOU WON")
            break


