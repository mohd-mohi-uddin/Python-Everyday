>>DAY 2 OF CODE:

>> CONDITIONAL STATEMENTS, LOGICAL OPERATIONS, CODE BLOCKS AND SCOPE.

--if and else statements:
these satements are used when we need to select weather a or b.
syntax of if else:
      
      if condition:
          print()
      else:
          print()

you can use comparision operators in the if else statements

>> COMPARISION OPERATORS:

'>'
<
'>='
<=
==
!=>

>> MODULO OPERATOR (%):

this operator gives the reminder when division is performed 

>> make a roller coster height check ticket code using if else statement:

height = int(input("enter your height in cm?"))

if height >= 120:
    print("you are ALLOWED to ride the roller coster")
else:
    print("you are NOT ALLOWED to ride the roller coster")

>> CHECK FOR ANY NUMBER WHICH IS EVEN OR ODD?

number = int(input("enter the number\n"))

if number % 2 == 0:
    print("even")
else:
    print('odd') 

>> NESTED IF/ELSE AND ELIF STATEMENTS:

so to add another condition in if else statement we use nested statements
syntax:

if condition:
    print()

    #the below code runs when the above if statement is true. u can add multiple elif statements in between.

    if condition:
        print()
    elif condition:
        print()
    else:
        print()
else:
    print() 

>> MULTIPLE IF STATEMENTS:

You can write as many if statements as you need to check for different conditions that are unrelated to each other. Compare the code blocks below:

If/elif/else
if condition 1 is true
    do A
elif condition 2 is true
    do B
else
    do C

Nested if statements
if condition 1 is true>
    do A>
    if condition 2 is true>
        do B>
        if condition 3 is true>
            do C>

>> LOGICAL OPERATORS:
 
and 
or
not

used for multiple conditions like: 
condition1 and condition2:
condition1 or condition2:
not condition:

>> RANDOMIZING:

to get random values we use randomizing so to do that there is a module created by the pyhton team which is used to import the random definations from the random module. 
here are the most used three calls which are:

>random.randit(a, b)
here its is used for integers.
we can give any random values to a and b and we can get between values from it including a and b.

>random.uniform(a, b)
here it is used for float values.
same as we use for integers.

>random.random()
it gives floating values between 0.0 and 1.0

>random.choice()
used when there is sequence is to used like lists.

now lets make a head and tails game using the following:

import random
coin = random.randit(0, 1)
if coin == 1:
     print("heads")
else:
    print("tails")

>> NESTED LISTS:

 we can easily add two list in one list for ex:
 list1 = [a,b,c]
 list2 = [d,e,f]
 we can nest this two list in one variable
 list = [list1,list2]

 if we use print(list[1][1])
 these meanse first [1] will take u to list 2 and then second [1] will take u to to index 1 of list 2.

 we can also chnage the contents of list using index like
 list[0] = apple
 now in the list whatever is there at index 0 is relpaced by apple.
