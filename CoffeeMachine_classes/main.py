from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

shut_down=False
while not shut_down:
    options=menu.get_items()
    choice=input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    if choice=='off':
        shut_down=True
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
    selected_drink=input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    drink=menu.find_drink(selected_drink)


    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
    else:
        print("Sorry that's not enough money. Money refunded.")
        shut_down=True
