coffee_menu = [
    {
        "name": "Espresso",
        "price": 1.50,
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        }
    },
    {
        "name": "Latte",
        "price": 2.50,
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        }
    },
    {
        "name": "Cappuccino",
        "price": 3.00,
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        }
    }
]

resources={
    "water":300,
    "milk":200,
    "coffee":100,
    "Profits Earned":0
}

def currency():
    print("Please enter coins for Transaction")
    quarters=int(input("How many quarters(25 cents) do you have sir "))*25
    nickels = int(input("How many nickels(5 cents) do you have sir "))*5
    dimes = int(input("How many dimes(10 cents) do you have sir "))*10
    penny = int(input("How many penny do you have sir "))*1
    return (quarters+nickels+dimes+penny)/100

def item_return(menu, choice):
    for item in menu:
        if item["name"].lower() == choice.lower():
            return item
        else:
            continue


def report():
    print(f"milk is {resources['milk']}")
    print(f"water is {resources['water']}")
    print(f"coffee is {resources['coffee']}")
    print(f"current profits are   {resources['Profits Earned']}")

def check_availability(resources,choice):
    item_chosen = item_return(coffee_menu, choice)
    if  item_chosen["ingredients"]["milk"]<=resources["milk"] and item_chosen["ingredients"]["water"]<=resources["water"] and item_chosen["ingredients"]["coffee"]<=resources["coffee"]:
        return True
    else:
        return False

def menu(resources,coffee_menu):
    report()
    print("\n")
    for item in coffee_menu:
        print(item['name'])
        print(f"milk is at {item['ingredients']['milk']}")
        print(f"water is at {item['ingredients']['water']}")
        print(f"coffee is at {item['ingredients']['coffee']}")
        print("\n")


def coffee_project():
    print("Welcome to the cafe coffee day sir , please choose Espresso,Latte,Cappuccino ")
    menu(resources,coffee_menu)
    choice = str(input("So what would you like sir "))

    if choice.lower=="off":
        print("Well Sorry but restaurent is closed sir ")
    elif choice.lower() in ["espresso", "latte", "cappuccino"]:
        values_worth = currency()
        balance = 0
        item_chosen = item_return(coffee_menu, choice)
        availability=check_availability(resources,choice)


        if not availability:
            print("Sorry Sir there arent enough materials for this sir ")
        elif values_worth >= item_chosen["price"]:
            if choice.lower() == "espresso".lower():
                print("Well get ready for some delicious espresso ")
                resources["milk"] = resources["milk"] - item_chosen["ingredients"]["milk"]
                resources["water"] = resources["water"] - item_chosen["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - item_chosen["ingredients"]["coffee"]
                resources["Profits Earned"] += item_chosen["price"]
                balance = values_worth - item_chosen["price"]
                print(f"current balance is {values_worth-item_chosen['price']}")


            elif choice.lower() == "Latte".lower():
                print("Well get ready for some delicious latte ")
                resources["milk"] = resources["milk"] - item_chosen["ingredients"]["milk"]
                resources["water"] = resources["water"] - item_chosen["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - item_chosen["ingredients"]["coffee"]
                resources["Profits Earned"] += item_chosen["price"]
                balance = values_worth - item_chosen["price"]
                print(f"current balance is {values_worth-item_chosen['price']}")


            elif choice.lower() == "Cappuccino".lower():
                print("Well get ready for some delicious cappuccino ")
                resources["milk"] = resources["milk"] - item_chosen["ingredients"]["milk"]
                resources["water"] = resources["water"] - item_chosen["ingredients"]["water"]
                resources["coffee"] = resources["sugar"] - item_chosen["ingredients"]["coffee"]
                resources["Profits Earned"] += item_chosen["price"]
                balance = values_worth - item_chosen["price"]
                print(f"current balance is {values_worth-item_chosen['price']}")

        else:
            print(f"SORRY SIR YOU DONT HAVE ENOUGH BALANCE TO SHOP SIR")

    elif choice.lower() == "report":
        report()


customers_arrival=True
coffee_machine_open=True

while customers_arrival and coffee_machine_open:
    open=str(input("Sir enter off for turning of machine or go for continue"))
    if open=="off":
        coffee_machine_open=False
        break
    elif open=="go":
        print("\n"*70)
        print("There you go")

    coffee_project()
    more=str(input("Are there any more customers ?"))
    if more.lower()=="no":
        customers_arrival=False
    else:
        print("\n"*100)
