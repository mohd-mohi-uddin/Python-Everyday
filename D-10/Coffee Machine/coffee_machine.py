MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resoursce_sufficient(order_resources):
    for item in order_resources:
        if resources[item] < order_resources[item]:
            print(f"sorry we are out of {item}")
            return False
        return True
    
def process_coins():
    print("insert coins:")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def payment_successful(coffee_price,money_recived):
    if coffee_price <= money_recived:
        change = money_recived - coffee_price
        print(f"here is your {change}")
        global profit
        profit += coffee_price
        return True
    else:
        print("sorry thats not enough money, Money refunded!")
        return False
    
def make_coffee(drink_name,order_resources):
    for item in order_resources:
        resources[item] -= order_resources[item]
    
    print(f"enjoy your {drink_name}")

is_on = True

while is_on:
    choice = input("what do you want? (latte,cappuccino,espresso):")

    '''this is the end of loop'''
    if choice == "off":
        is_on = False
    
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"profit: {profit}$")
    
    else:
        drink = MENU[choice]

        if is_resoursce_sufficient(drink["ingredients"]):
            amount = process_coins()
            if payment_successful(drink["cost"],amount):
                make_coffee(choice,drink["ingredients"])
            
