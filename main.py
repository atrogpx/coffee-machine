from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True
while on:
    req = input("What would you like? " + menu.get_items())
    if req == "report":
        coffee_maker.report()
        money_machine.report()
    elif req == "off":
        on = False
    else:
        order = menu.find_drink(req)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)