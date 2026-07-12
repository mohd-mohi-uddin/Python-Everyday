>>> ITERROWS IN PANDAS:

iterrows() is a Pandas DataFrame method used to iterate through a DataFrame row by row.

Syntax
for index, row in dataframe.iterrows():
    # use row
index → The row number (or index label).
row → A Series containing that row's data.
Example
import pandas as pd

data = {
    "Name": ["Asim", "John", "Emma"],
    "Age": [22, 20, 21]
}

df = pd.DataFrame(data)

for index, row in df.iterrows():
    print(index)
    print(row)

Output:

0
Name    Asim
Age       22
Name: 0, dtype: object

1
Name    John
Age       20
Name: 1, dtype: object

2
Name    Emma
Age       21
Name: 2, dtype: object


