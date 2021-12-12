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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resourses(selection, drink_to_dispense):
    # Water
    ingredients = drink_to_dispense["ingredients"]
    #print(ingredients)
    if ingredients["water"] <= resources["water"]:
        return True
    else:
        print("Sorry there is not enough water.")
        return False
    if not(selection == "espresso"):
        if ingredients["milk"] <= resources["milk"]:
            return True
        else:
            print("Sorry there is not enough milk.")
            return False
    if ingredients["coffee"] <= resources["coffee"]:
        return True
    else:
        print("Sorry there is not enough coffee.")
        return False

def get_resourses(selection, drink_to_dispense):
    ingredients = drink_to_dispense["ingredients"]
    resources["water"] = resources["water"] - ingredients["water"]
    if not (selection == "espresso"):
        resources["milk"] = resources["milk"] - ingredients["milk"]
    resources["coffee"] = resources["coffee"] - ingredients["coffee"]


def process_coins(selection,drink_to_dispense):
    global money
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    total_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    if total_coins >= drink_to_dispense['cost']:
        get_resourses(selection, drink_to_dispense)
        print(f"Here is ${round((total_coins - drink_to_dispense['cost']),2)} in change.")
        print(f"Here is your {selection} ☕️. Enjoy!")
        money += drink_to_dispense['cost']
    else:
        print("Sorry that's not enough money. Money refunded.")

money = 0
machine_on = True

while machine_on:

    selection = input("What would you like? (espresso/latte/cappuccino): ")


    if selection == "espresso" or selection == "latte" or selection == "cappuccino":
        drink_to_dispense = MENU[selection]
        print(drink_to_dispense)
        if check_resourses(selection, drink_to_dispense):
            process_coins(selection, drink_to_dispense)
    elif selection == "report":
        for item in resources:
            print(f"{item.capitalize()}: {resources[item]}")
        print(f"Money: ${money}")
    elif selection == "off":
        machine_on = False
    else:
        print("Wrong selection")


