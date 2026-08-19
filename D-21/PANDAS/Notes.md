>>> CSV FILES:

Csv files are the formatted form of tabular data
where each coloumn and rows are sepearted with commas.

The full form of csv is comma seperated values.

>>> PATHLIB:
u can use the path lib to locate paths of your files. using syntax:

from pathlib import Path

storing variable = path(__file__).parent.

thats it now this will take you to the parent of that file.

>>> LIST comprehension:

numbers = [1, 2, 3, 4]

new_list = []

for num in numbers:
    new_list.append(num * 2)

List comprehension:

new_list = [num * 2 for num in numbers]

Output:

[2, 4, 6, 8]