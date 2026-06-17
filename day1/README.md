#DAY 1 OF CODE:


1. print function print()
we saw that we need to write print() and in () we have to write the sring with "" or we can write variable names 

2. string manipulation 
we learnt howto concatinate two strings using "+"

3. Input fuction input()
we can give input in the terminal using the input function
name = input("whats your name?\n")

4. lenght of string len()
we can use this to know the lenght of the string

5. variable naming 
rules: 
*no spaces between variables
*no varbile must start with letters 
*use _ to add space between characters 
*dont use key words as variables 

>>> DATA TYPES, NU MBERS, OPERATIONS, TYPE CONVERTION, F-STRINGS


 Subscripting
 ptint("hello"[0])
 the output will be "h" because we use [] this for indexing and indexing always starts from 0. we can also do slicing using indexing.

 >> DATA TYPES:
 
 String 
 any this which is written between " " is a string 

 Integer 
 print(124 + 234)

 Float 
 print(123.05)

 boolean
 print(true)
 print(false)

>> TYPE CHECKING:

to check the type of data we use type() function
name = "asim" 
print(type(name))

>> TYPE CONVERSION:

-if we try to concatinate a str with int its not possible but if we want to do so we can change the type of one of the data type.
-we can do this by using int(), str(), float() functions
for example we can 

print("Number of letters in your name: " + len(input("Enter your name")))

here first is str and second in int 
to work this we must change int to str making 
len(input("Enter your name")) to
str(len(input("Enter your name")))

>> OPERATORS:

there five mathematical operators which are:
*
/
//
+
-

in // the division is done bu the decimals we got are removed 

the operators in the python got priorities
PEMDAS
where p is parethesis()
e is exponents **
m is multiplication *
d is divison /
a is addition + 
s is subraction - 

>> FLOORING A NUMBER:

You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).

int(3.738492) # Becomes 3

>> ROUNDING A NUMBER:

However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.

round(3.738492) # Becomes 4

round(3.14159) # Becomes 3

round(3.14159, 2) # Becomes 3.14

>> ASSIGMENT OPERATORS:

Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

+=

-=

*=

/=

>> F-STRINGS:

In Python, we can use f-strings to insert a variable or an expression into a string.
age = 12
print(f"I am {age} years old")
Will output I am 12 years old.