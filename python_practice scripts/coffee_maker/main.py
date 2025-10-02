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

def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]

    for key in ingredients:
        if resources[key] < ingredients[key]:
            print(f"Sorry there is not enough {key}")
            return
        else:
            resources[key] -= ingredients[key]

def payment():
    total = 0
    print("Please insert coins.")
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def payment_process(payment_total, user_drink):
    coffe_cost = MENU[user_drink]["cost"]

    if payment_total > coffe_cost:
        change = round(payment_total - coffe_cost, 2)
        print(f"Here is your change: ${change}")
        resources["money"] += coffe_cost
    elif payment_total == coffe_cost:
        resources["money"] += coffe_cost
    else:
        print(f"Not enough money to buy coffe")



def coffee_machine():
    coffee_machine_is_on = True
    resources["money"] = 0

    while coffee_machine_is_on:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        if user_input == "off":
            coffee_machine_is_on = False

        elif user_input == "report":
            report()

        elif user_input in MENU:
            make_coffee(user_input)
            payment_process(payment(), user_input)

        else:
            print("Please choose something from the menu")


coffee_machine()