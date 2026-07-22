import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("\nHow many letters would you like in your password?\n"))
nr_symbols = int(input(f"\nHow many symbols would you like?\n"))
nr_numbers = int(input(f"\nHow many numbers would you like?\n"))
    
random_letters = random.choices(letters, k = nr_letters)
random_symbols = random.choices(symbols, k = nr_symbols)
random_numbers = random.choices(numbers, k = nr_numbers)
# used random.choices insted of sample because i want repeated characters.

combined = random_letters + random_symbols + random_numbers
random.shuffle(combined)
result ="".join(combined)
print(f'\nyour password is:\n{result}')

