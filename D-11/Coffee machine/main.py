from menu import Menu 
from menu import MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    choice = input("what do u like to have(latte,cappuccino,espresso):")

    if choice == "report":
        coffeemaker.report()
        moneymachine.report()

    elif choice == "off":
        is_on = False

    else:
        drink = menu.find_drink(choice)

        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
