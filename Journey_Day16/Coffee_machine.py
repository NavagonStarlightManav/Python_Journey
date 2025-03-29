from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

customers_arrival=True
coffee_machine_open=True

while customers_arrival and coffee_machine_open:
    open=str(input("Sir enter off for turning of machine or go for continue"))
    if open == "off":
        coffee_machine_open = False
        break
    elif open == "go":
        print("There you go sir , Most welcome sir ")



    print(f"Todays specials are {menu.get_items()}")
    choice = str(input("So what would you like sir "))

    if choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_ordered = menu.find_drink(choice)
        resource_sufficient = coffee_maker.is_resource_sufficient(drink_ordered)
        if resource_sufficient:
            cost = drink_ordered.cost
            transaction_success = money_machine.make_payment(cost)
            if transaction_success:
                coffee_maker.make_coffee(drink_ordered)



    more = str(input("Are there any more customers ?"))
    if more.lower() == "no":
        customers_arrival = False
    else:
        print("\n" * 100)