>>Exception Handling:

Syntax
try:
    # Code that may cause an error

except ErrorType:
    # Runs if that error occurs

else:
    # Runs only if NO error occurs

finally:
    # Always runs


>>try
Contains code that might raise an exception.
Python attempts to execute it.
try:
    num = int(input())


>>except
Runs only if an error occurs.
Prevents the program from crashing.
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero.")


>>else
Runs only if the try block succeeds (no exceptions).
try:
    num = int(input())
except ValueError:
    print("Invalid input")
else:
    print("Success")


>>finally
Runs every time, whether an error occurs or not.
Commonly used for cleanup (closing files, database connections, etc.).
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Program finished")


>>Common Exceptions:

ValueError	
TypeError	
IndexError	
KeyError	
FileNotFoundError	
ZeroDivisionError	

>> CSV(DATA FRAME) TO DICT: ORIENTATION

1. orient="dict" (Default)
df.to_dict()
{
    "Name": {0: "Alice", 1: "Bob"},
    "Age": {0: 20, 1: 25}
}
2. orient="list"
df.to_dict("list")
{
    "Name": ["Alice", "Bob"],
    "Age": [20, 25]
}
3. orient="series"
df.to_dict("series")
{
    "Name": Series(...),
    "Age": Series(...)
}

Each value is a Pandas Series.

4. orient="records" ⭐ (Most common)
df.to_dict("records")
[
    {"Name": "Alice", "Age": 20},
    {"Name": "Bob", "Age": 25}
]

Each row becomes a dictionary.

5. orient="index"
df.to_dict("index")
{
    0: {"Name": "Alice", "Age": 20},
    1: {"Name": "Bob", "Age": 25}
}

Here the index is the key.

6. orient="split"
df.to_dict("split")
{
    "index": [0, 1],
    "columns": ["Name", "Age"],
    "data": [
        ["Alice", 20],
        ["Bob", 25]
    ]
}

Everything is separated into index, columns, and data.

7. orient="tight"
df.to_dict("tight")
{
    "index": [0, 1],
    "columns": ["Name", "Age"],
    "data": [
        ["Alice", 20],
        ["Bob", 25]
    ],
    "index_names": [None],
    "column_names": [None]
}

This includes extra metadata about the index and column names.