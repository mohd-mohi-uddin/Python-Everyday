>> FUNCTIONS WITH INPUTS:

so we can use functions with giving them inpuits inside their paranthesis. in the paranthesis we need to pass on a variable ehich will aslo be used in the body of function. we call this variable as parameters in functions.

wen ever we call that function we need to give value to that parameter which is called as argument.

for example:
def greet(name):
   print(f"how are ypu {name}?")

>with one argument:

greet(asim)

output = how are you asim?

>with two arguments:

for example:
def greet(name,location):
   print(f"how are ypu {name}?")
   print(f"how is the weather in {location}")

greet(location = india,name = asim)

>>>IMPORTANT NOTE:
>> LIST AND STRINGS:

u cannot find a list in string

but u can do string in list

u can also do string in string

>note: if there is a sitation where u need to search some letters in string then u can iterate the string and then search for the letters

for example:

name = "mohd mohiuddin"
letters = "mdin"
to do this use for loop to iterate over name

for i in name:

this will make your name look
m
o
h
d

m
o
.
.

now u can type 
if i in letters:

means if the m,o,h,d,m,o,h,i,u,d,d,i,n are in mdin 

now add the letters that match m,d,i,n in an empty string
empty_string += i

example code:


def calculate_love_score(name1, name2):
    name = (name1+name2).lower()
    count1 = ""
    count2 = ""
    check1 = "true"
    check2 = "love"
    for i in name:
        if i in check1:
            count1 += i
    for j in name:
        if j in check2:
            count2 += j
        
    letters_in_count1 = len(count1)
    letters_in_count2 = len(count2)
    print(f"{letters_in_count1}{letters_in_count2}")
    
calculate_love_score("Kanye West", "Kim Kardashian")

>> MORE USES OF FOR LOOPS:

u an iterate over a string and get it index all at a time and then can chage their indices inside the iteration 
for example:
for i in message:
   message.index(i)
