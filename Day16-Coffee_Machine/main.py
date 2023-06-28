from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()


make_coffee = CoffeeMaker()
money_changer = MoneyMachine()
end_of_machine = False
# choice를 인자로 해서, find_drink()에 넣으면 메뉴가 있는지 없는지 확인해 줌.
while not end_of_machine:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "report":
        make_coffee.report()
        money_changer.report()
    elif choice == "off":
        end_of_machine = True
    else:
        drink = menu.find_drink(order_name=choice)
        if make_coffee.is_resource_sufficient(drink=drink):
            if money_changer.make_payment(drink.cost):
                make_coffee.make_coffee(drink)



