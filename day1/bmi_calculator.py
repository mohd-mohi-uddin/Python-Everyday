#BMI CALCULATOR

print("CALCULATE YOUR BMI:\n")
height = float(input("enter your height in meters:\n"))
weight = float(input('enter your weight in Kgs:\n'))
print('\nyour BMI is:')
bmi = weight / (height**2)
print(int(bmi))
if bmi < 18.5:
    print('you are underweight')
elif bmi <= 25:
    print('you have a normal weight')
else:
    print('you are overweight')