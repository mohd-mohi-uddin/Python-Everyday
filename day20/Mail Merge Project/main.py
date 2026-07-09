from pathlib import Path

BASE_DIR = Path(__file__).parent

placeholder = "[name]"

with open(BASE_DIR /'input' /'names' /'invited_names.txt') as file:
    names = file.readlines()
 
with open(BASE_DIR /'input' /'letter' /'starting_letter.txt') as letter:
    contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = contents.replace(placeholder,stripped_name)
        with open(BASE_DIR /'output' /'ready_to_send' /f'letter_for_{stripped_name}.docx',mode="w") as single_letter:
            single_letter.write(new_letter)

        

