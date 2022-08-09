from data import coffees,machine_resources,coins

def machine_sufficient():
    """Checks if the machine resources are insufficient"""

    for item in resource_keys:
        if machine_resources[item]<drink[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def check_coins():
    """Returns the amount of coins inserted into the machine"""
    
    print("Please insert coins")
    quarters=int(input("How many quarters? :"))
    dimes=int(input("How many dimes? :"))
    nickles=int(input("How many nickles? :"))
    pennies=int(input("How many pennies? :"))
    return quarters*coins['quarter']+dimes*coins['dime']+nickles*coins['nickel']+pennies*coins['penny']

shut_down=False
while not shut_down:
    resource_keys=["water","milk","coffee"]
    choice=input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    if choice=='off':
        shut_down=True
    elif choice=="report":

        print(f"Water: {machine_resources['water']}ml \nMilk: {machine_resources['milk']}ml \nCoffee: {machine_resources['coffee']}gr \nMoney: ${machine_resources['money']}")

        selected_drink=input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
        drink=coffees[selected_drink]

        if machine_sufficient():
            amount=check_coins()
            if amount>=drink['price']:
                change="{:.2f}".format(amount-drink["price"])
                print(f"Here is ${change} change.")
                print(f"Here is your {selected_drink}.☕ Enjoy!")

                #update machine resources
                for item in resource_keys:
                    machine_resources[item]-=drink[item]

                machine_resources["money"]+=drink["price"]
            else:
                print("Sorry that's not enough money. Money refunded.")
                shut_down=True



