from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTERS = 0.25
DIMES = 0.10
NICKEL = 0.05
PENNIES = 0.01

money = 0


# print report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


# process coins
def process_coins():
    quarters = float(input("How many quarters?: ")) * QUARTERS
    dimes = float(input("How many dimes?: ")) * DIMES
    nickles = float(input("How many nickles?: ")) * NICKEL
    pennies = float(input("How many pennies?: ")) * PENNIES
    return quarters + dimes + nickles + pennies


# check resource sufficient
def is_resource_sufficient(choice):
    needed_water = MENU[choice]['ingredients'].get('water', 0)
    needed_milk = MENU[choice]['ingredients'].get('milk', 0)
    needed_coffee = MENU[choice]['ingredients']['coffee']
    if resources['water'] >= needed_water:
        if resources['milk'] >= needed_milk:
            if resources['coffee'] >= needed_coffee:
                return True
            else:
                print("Sorry, there is not enough coffee.")
                return False
        else:
            print("Sorry, there is not enough milk.")
            return False
    else:
        print("Sorry, there is not enough water.")
        return False


# check inserted enough money
def enough_money(inserted_money, coffee_cost):
    global money
    if inserted_money == coffee_cost:
        money += coffee_cost
        return True
    elif inserted_money > coffee_cost:
        change = inserted_money - coffee_cost
        money += coffee_cost
        print(f"Here is ${round(change, 2)} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# make coffee
def make_coffee(choice):
    resources['water'] -= MENU[choice]['ingredients'].get('water', 0)
    resources['milk'] -= MENU[choice]['ingredients'].get('milk', 0)
    resources['coffee'] -= MENU[choice]['ingredients']['coffee']
    print(f"Here is your {choice}. Enjoy!")


# Main loop
enough_resources = True
while enough_resources:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        print_report()
    elif user_choice == 'off':
        enough_resources = False
    elif user_choice in MENU:
        if is_resource_sufficient(user_choice):
            print("Please insert coins.")
            monetary_value = process_coins()
            if enough_money(monetary_value, MENU[user_choice]['cost']):
                make_coffee(user_choice)
        else:
            enough_resources = False
    else:
        print("Invalid choice. Please select again.")
