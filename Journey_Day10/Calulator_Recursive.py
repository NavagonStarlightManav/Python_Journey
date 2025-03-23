calculator_art = """
  ██████╗ █████╗ ██╗      ██████╗██╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗ 
 ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
 ██║     ███████║██║     ██║     ██║   ██║███████║   ██║   ██║   ██║██████╔╝
 ██║     ██╔══██║██║     ██║     ██║   ██║██╔══██║   ██║   ██║   ██║██╔═══╝ 
 ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║     
  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     
  ┌─────────────────┐
  │  [7] [8] [9]  ÷ │
  │  [4] [5] [6]  × │
  │  [1] [2] [3]  - │
  │  [0] [C] [=]  + │
  └─────────────────┘
"""
Welcome=calculator_art+"\n"+"Welcome to the calculator app , let's see if we can make your life easy with calculations"
print(Welcome)

def add(a,b):
    return a+b
def subract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations={
    "+":add,
    "-":subract,
    "*":multiply,
    "/":divide,
}


def Calc():
    calculator_in_running = True
    num1 = float(input("Please enter first number "))

    while calculator_in_running:

        num2 = float(input("Please enter second number "))
        operation_symbol = str(input("Please enter the operation you want to do "))
        result = operations[operation_symbol](num1, num2)
        print(f"The result of {num1} {operation_symbol} {num2} = {result}")

        continue_choice = str(input(
            "Please enter 'yes' if you want to continue with previous value and 'new' if you want to continue from start and 'stop' for stopping the game"))
        if continue_choice.lower() == "yes":
            num1=result

        elif continue_choice.lower() == "new":

            print('\n'*100)
            print(Welcome)
            Calc()
        else:
            calculator_in_running = False

Calc()

