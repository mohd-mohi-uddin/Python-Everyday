>> READ,WRITE AND APPEND WITH FILES:

1. What is a file?

A file is simply something stored on your computer.

For example:

day16/
│── snake_game.py
│── scorecard.py
│── data.txt

data.txt might contain:

15

or

Hello World

Python can:

Read from it 📖
Write to it ✍️
2. Opening a file

Use open().

file = open("data.txt")

Now file represents the opened file.

3. Reading a file
file = open("data.txt")

content = file.read()

print(content)

file.close()

Suppose data.txt contains:

25

Output:

25
4. Why close()?

When Python opens a file, the operating system keeps it open.

Always close it.

file.close()

Otherwise resources stay allocated longer than necessary.

5. Better way: with

Instead of:

file = open("data.txt")

content = file.read()

file.close()

use

with open("data.txt") as file:
    content = file.read()

print(content)

When the with block finishes:

Open

↓

Read

↓

Automatically Close

This is the recommended way.

6. Writing to a file

Use mode "w".

with open("data.txt", mode="w") as file:
    file.write("100")

Now data.txt contains:

100
Important

Writing mode erases everything first.

Suppose:

data.txt

15

Then

with open("data.txt", "w") as file:
    file.write("100")

becomes

100

The old value 15 is gone.

7. Appending

If you want to keep the old data:

with open("data.txt", "a") as file:
    file.write("\nHello")

Suppose the file had:

15

Now it becomes:

15
Hello

Nothing was erased.

8. Reading numbers

Suppose

data.txt

25

Reading:

with open("data.txt") as file:
    score = file.read()

score becomes

"25"

Notice the quotes.

It is a string.

Convert it:

score = int(score)

Now

score

is

25

(an integer)

9. Writing numbers

Suppose

score = 30

This won't work:

file.write(score)

because write() only accepts strings.

Convert it:

file.write(str(score))

Now Python writes:

30

>>>> FILE MODE:

we can set mode as read write append using the mode in the open(filename, mode as "w", "r" amd "a") by using this we can 
perform operations on files.

>>>> FILE FUNCTIONS:

there are three functions we can use on file to make it more easy for file editing

1. file.readline() this takes ever line of the file as the item of list. 
suppose the file has lines then it makes 6 items in the lists.

2. file.replace(word to replace, new word): this replaces the word with the given word 
in the text file.

3. file.strip(): this function removes any extra spaces, unwanted things from the given string

