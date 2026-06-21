>> SYNTAX FOR IF/ELSE, FOR AND WHILE LOOP:

These are the most important forms you'll use as a Python beginner.

>1. if

Runs code only when a condition is True.

age = 20

if age >= 18:
    print("Adult")

Meaning:

If age is 18 or more, print "Adult".

>2. if else

Two possible paths.

age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")

Meaning:

If condition is True do first block, otherwise do second block.

>3. if elif else

Multiple choices.

score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")

Python checks from top to bottom and stops at the first True condition.

>4. Nested if

An if inside another if.

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("Enter")

Meaning:

First check age, then check ticket.

>5. for loop with a list
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

Output:

apple
banana
mango

Meaning:

Take each item one by one.

>6. for loop with a string
word = "cat"

for letter in word:
    print(letter)

Output:

c
a
t

Meaning:

Take each character one by one.

>7. for loop with range()
for number in range(5):
    print(number)

Output:

0
1
2
3
4
Start and stop
for number in range(1, 6):
    print(number)

Output:

1
2
3
4
5
Step
for number in range(0, 11, 2):
    print(number)

Output:

0
2
4
6
8
10

>8. while loop

Runs while a condition is True.

count = 1

while count <= 5:
    print(count)
    count += 1

Output:

1
2
3
4
5

Meaning:

Keep repeating until count becomes greater than 5.

>9. Infinite while loop
while True:
    print("Hello")

Runs forever.

Usually used with break.

>10. while True + break
while True:
    password = input("Enter password: ")

    if password == "python":
        break

Meaning:

Keep asking until correct password.

>11. continue

Skip current iteration.

for number in range(5):

    if number == 3:
        continue

    print(number)

Output:

0
1
2
4

Python skips 3.

>12. break

Stop loop immediately.

for number in range(10):

    if number == 5:
        break

    print(number)

Output:

0
1
2
3
4

Loop stops at 5.

>13. For loop with index
word = "cat"

for i in range(len(word)):
    print(i, word[i])

Output:

0 c
1 a
2 t

Useful in Hangman.

Quick Rule
Use if

When making decisions.

if age > 18:
Use for

When you know what to iterate through.

for letter in word:
Use while

When you don't know how many times it will run.

>> Most important patterns to memorize

if condition:

if condition:
else:

if condition:
elif condition:
else:

for item in collection:

for i in range(start, stop, step):

while condition:

while True:
    if something:
        break