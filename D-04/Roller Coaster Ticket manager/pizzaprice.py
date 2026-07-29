
print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ").upper()
while True:
    if size == "S":
        bill = 15
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
        if pepperoni == "Y":
            bill += 2
        break
    elif size == "M":
        bill = 20
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()  
        if pepperoni == "Y":
            bill += 3
        break
    elif size == "L":
        bill = 25
        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()  
        if pepperoni == "Y":
            bill += 3
        break
    else:
        print("type error, please type S,M and L only.")
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()  
if extra_cheese == "Y":
    bill += 1
print(bill)
