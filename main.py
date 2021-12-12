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

def get_resourses(selection, drink_to_dispense):
    # Water
    ingredients = drink_to_dispense["ingredients"]
    #print(ingredients)
    if ingredients["water"] <= resources["water"]:
        print("Ok")
    if not(selection == "espresso"):
        if ingredients["milk"] <= resources["milk"]:
            print("Ok")
    if ingredients["coffee"] <= resources["coffee"]:
        print("Ok")

def process_coins(selection,drink_to_dispense):
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
    else:
        print("Sorry that's not enough money. Money refunded.")

selection = input("What would you like? (espresso/latte/cappuccino): ")
money = 0

if selection == "espresso" or selection == "latte" or selection == "cappuccino":
    drink_to_dispense = MENU[selection]
    print(drink_to_dispense)
    process_coins(selection, drink_to_dispense)
elif selection == "report":
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}")
    print(f"Money: ${money}")
else:
    print("Wrong selection")


