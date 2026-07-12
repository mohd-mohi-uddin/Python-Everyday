import pandas
from pathlib import Path

BASE_DIR = Path(__file__).parent

data = pandas.read_csv(BASE_DIR /"nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for index,row in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name:").upper()
output_list = [new_dict[i] for i in user_input]
print(output_list)
