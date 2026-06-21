#Day 4 of code:

>> FUNCTIONS:

functions are the set of code which can be used any time. when u call that function the code inside it runs automatically there is no need of writing the code again.

their are many built in functions in python but u can make your own function.

the syntax for making a function is:
1. def function():
2.     body
3. function()

in the first line we need to define function using def and then the funtion name and then two parenthisis.

in the second line u need to write the body of function whuch code and it must be indented inside the function.

after writing the body. when ever u need to call the body u need to type function name and then two parenthisis.

>> WHILE LOOPS:

A while loop is a control structure that repeatedly executes a block of code as long as a condition is true.

Syntax:

while condition:
    # code to execute
Example 1: Counting from 1 to 5

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

if while loop can become a infinte loop if the given condition is true so need a "break" statement in the end of the body.

syntax for break:

while True:
    name = input("Enter your name: ")

    if name == "quit":
        break

    print("Hello", name)

print("Loop ended")

