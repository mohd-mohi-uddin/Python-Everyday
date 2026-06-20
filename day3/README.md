>> LOOPS:

There are two types of loops in Python, for and while.

The "for" loop
For loops iterate over a given sequence. Here is an example:

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

>> SYNTAX FOR LOOPS:

for loop
for i in varible:
    print()

>> RANGE IN LOOPS:

the range is a function which shoukd be use in combination with with other function like loops
Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

Prints out 3,4,5
for x in range(3, 6):
    print(x)

Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

>to do 1+2+3+4+...till 100 u can do

adding = 0
for number in range(1,101):
    adding += number
print(adding)

> to print the highest in list using for loop:

you can do this with max() function also

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)

>>> TOPIC FROM RANDOMIZATION:

>> random.choices vs random.choices vs random.sample

in the the ramdom.choice u can only get one element form list

but in random.choices and random.sample u can get multiple iteams 

and in random.choices u can get repeated iteams but in sample u dont get repeated items.

>> RANDOM.SHUFFLE()

its shuffles the iteams of the list
used only for list 
and its syntax for list is

list = []
random.shuffle(list)
print(list)

not

result = random.shuffle(list)
print(result) #it shoes none.

>> "".join(list)

it joins only strings if they are in a sequence
like ["A", "b"] as Ab.

>> you can convert a string to list using for loop also from string to list.

>string to list:

char = "55678"
text = []
for i in char:
    text.append(i)
print(text)

>list to string:

char = ['5', '5', '6', '7', '8']
text = ""
for i in char:
    text += i
print(text)
