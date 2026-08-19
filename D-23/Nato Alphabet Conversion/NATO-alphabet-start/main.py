import pandas
from pathlib import Path

BASE_DIR = Path(__file__).parent

data = pandas.read_csv(BASE_DIR /"nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for index,row in data.iterrows()}

def generate_letters():
    user_input = input("Enter your name:").upper()
    try:
        output_list = [new_dict[i] for i in user_input]
    except KeyError:
        print("please enter only text")
        generate_letters()
    else:
        print(output_list)

generate_letters()