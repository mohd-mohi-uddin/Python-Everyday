#make a roller coster height check ticket code using if else statement:

height = int(input("\nEnter your height in cm?\n"))

if height >= 120:
    print("You are ALLOWED to ride the roller coaster")
    age = int(input("\nEnter your age:\n"))
    if age <= 12:
        bill = 5
        print("Child ticket is of 5$")
    elif age < 18:
        bill = 7
        print('Teen ticket is of 7$ ')
    else:
        bill = 12
        print("Adult ticket is for 12$")
    while True:
        take_photo = input("\nDo you want a photo of your ride? type 'y' if Yes or 'n' if No: \n").lower
        if take_photo == "y":
            bill += 3
            print(f'Your bill is: {bill}$')
            break
        elif take_photo == "n":
            print(f'Your bill is: {bill}$')
            break
        else:
            print("Type error, please enter only 'y' and 'n'") 

    
else:
    print("you are NOT ALLOWED to ride the roller coaster")