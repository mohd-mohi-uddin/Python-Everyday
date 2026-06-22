# def greet():
#     print("hello")
#     print("hello")
#     print("hello")
# greet()

def greet(name,location):
   print(f"how are you {name}?")
   print(f"how is the weather in {location}")

greet(location = "india", name = "asim")

# QQQQ. Love Calculator
# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out. 

# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times 

# R occurs 1 time 

# U occurs 2 times 

# E occurs 2 times 

# Total = 5 

# L occurs 1 time 

# O occurs 0 times 

# V occurs 0 times 

# E occurs 2 times 

# Total = 3 



# Love Score = 53





# Example Input 

# calculate_love_score("Kanye West", "Kim Kardashian")

# Example Output

# 42





# How to test your code and see your output?



# Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:



# def calculate_love_score(name1, name2):
#   # your code here
 
# # Call your function with hard coded values
# calculate_love_score("Kanye West", "Kim Kardashian")

#ANS:

def calculate_love_score(name1, name2):
    name = (name1+name2).lower()
    count1 = ""
    count2 = ""
    check1 = "true"
    check2 = "love"
    for i in check1:
        if i in name:
            count1 += i
    for j in check2:
        if j in name:
            count2 += j
        
    letters_in_count1 = len(count1)
    letters_in_count2 = len(count2)
    print(f"{letters_in_count1}{letters_in_count2}")
    
calculate_love_score("Kanye West", "Kim Kardashian")