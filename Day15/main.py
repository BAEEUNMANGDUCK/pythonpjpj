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
current_money = 0


def machine_report(cur_money):
    return f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${current_money}"


def check_resources(w, m, c, choice):
    need_ingredient = MENU[choice]['ingredients']  # water, milk, coffee
    for ingre in need_ingredient:
        if resources[ingre] < need_ingredient[ingre]:
            return 'False', ingre
    return 'True', None


def coin_sum():
    print("Please insert coins")
    coins = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    total = 0
    for coin in coins:
        total += int(input(f"how many {coin}?: ")) * coins[coin]
    return total


def check_transaction(coins, choice):
    menu_cost = MENU[choice]['cost']
    if coins < menu_cost:
        print("Sorry that's not enough money, Money refunded")
        return 'False', 0
    else:
        changes = coins - menu_cost
        print(f"Here is ${changes:.1f} in change")
        return 'True', menu_cost


def make_coffee(menu_choice):
    # global resources why?
    need_ingre = MENU[menu_choice]['ingredients']
    for ingre in need_ingre:
        resources[ingre] -= need_ingre[ingre]


def coffee_machine():
    global current_money

    # TODO 2: how to turn off the coffee machine?
    end_of_machine = False
    # TODO 1: Prompt user by asking "what would you like? (espresso/latte/cappuccino): "

    while not end_of_machine:
        choice = input("what would you like? (espresso/latte/cappuccino): ").lower()
        # TODO 3: Print Report
        if choice == 'report':
            print(machine_report(cur_money=current_money))
        elif choice == "off":
            end_of_machine = True
        # TODO 4: Check resources sufficient?
        elif choice in ["espresso", "latte", "cappuccino"]:
            order_available, not_enough = check_resources(resources['water'], resources['milk'], resources['coffee'],
                                                          choice)
            # print(bool(order_available))
            if order_available == 'True':
                total_coins = coin_sum()
                # TODO 6: Check transaction successful?
                transaction_success, profit = check_transaction(coins=total_coins, choice=choice )
                if transaction_success == 'True':
                    # TODO 5: Process coins.
                    current_money += profit
                    # TODO 7: Make Coffee
                    make_coffee(menu_choice=choice)

            else:
                print(f"Sorry there is not enough {not_enough}")

        else:
            print("Invalid Input")







coffee_machine()
