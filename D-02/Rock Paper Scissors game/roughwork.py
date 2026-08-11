#this is the code related to readme.md contents:

#make a roller coster height check ticket code using if else statement:

#height = int(input("enter your height in cm?"))

#if height >= 120:
#    print("you are ALLOWED to ride the roller coster")
#else:
#    print("you are NOT ALLOWED to ride the roller coster")

#CHECK FOR ANY NUMBER WHICH IS EVEN OR ODD?

#number = int(input("enter the number\n"))

#if number % 2 == 0:
#    print("even")
#else:
#    print('odd') 

# print("Welcome to Python Pizza Deliveries!")
# bill = 0
# size = input("What size pizza do you want? S, M or L: ").upper()
# while True:
#     if size == "S":
#         bill = 15
#         pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
#         if pepperoni == "Y":
#             bill += 2
#         break
#     elif size == "M":
#         bill = 20
#         pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()  
#         if pepperoni == "Y":
#             bill += 3
#         break
#     elif size == "L":
#         bill = 25
#         pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()  
#         if pepperoni == "Y":
#             bill += 3
#         break
#     else:
#         print("type error, please type S,M and L only.")
# extra_cheese = input("Do you want extra cheese? Y or N: ").upper()  
# if extra_cheese == "Y":
#     bill += 1
# print(bill)


# import random
# coin = random.randint(0, 1)
# if coin == 1:
#      print("heads")
# else:
#     print("tails")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[0])

# password = ""
# for char in range(0,nr_letters):
#     random_letters = random.choice(letters)
#     password += random_letters
# print(password)

# numbers = [3, 7, 2, 9, 3, 8]

# def largest_number(nums):
#     largest = numbers[0]
#     for num in nums:
#         if num > largest:
#             largest = num
      

#     return largest

# largest = largest_number(numbers)
# numbers.remove(largest)
# print(largest_number(numbers))

numbers = [5, 5, 5, 5]

def largest_and_2ndlargest_numbers(nums):
    biggest = None
    second_biggest = None

    for num in nums:
        if num > biggest: 
            second_biggest = biggest
            biggest = num

        elif num < biggest and second_biggest == None:
            second_biggest = num

        elif num < biggest and num > second_biggest:
            second_biggest = num

    return f"biggest:{biggest}, second biggest:{second_biggest}"

print(largest_and_2ndlargest_numbers(numbers))

        


            





