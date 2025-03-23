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
print(calculator_art)

print("Welcome to the calculator app , let's see if we can make your life easy with calculations ")

calculator_in_running=True

def Operations(first_num,second_num,operation):
    if operation=="+":
        return first_num+second_num
    elif operation=="-":
        return first_num-second_num
    elif operation=="*":
        return first_num*second_num
    elif operation=="/":
        return first_num/second_num
    else:
        print("Please enter correct operation sir ")
        return

def Run_Operations():
    num1 = int(input("Please enter first number "))
    num2 = int(input("Please enter second number "))
    operation = str(input("Please enter the operation you want to do "))

    result = Operations(num1, num2, operation)
    return result

result=Run_Operations()
print(f"The result of operations is {result}")

while calculator_in_running:
    continue_choice=str(input("Please enter 'yes' if you want to continue with previous value and 'new' if you want to continue from start and 'stop' for stopping the game "))

    if continue_choice.lower()=="yes":
        result=Operations(result,int(input("Please enter  the other number ")),str(input("Please enter the operation you want to do ")))
        print(f"The result is {result}")

    elif continue_choice.lower()=="new":
        print("\n"*50)
        print(calculator_art)
        print("Welcome to the calculator app , let's see if we can make your life easy with calculations ")

        result=Run_Operations()
        print(f"The result is {result}")

    elif continue_choice.lower()=="stop":
        calculator_in_running=False
    else:
        print("Please proceed correctly ahead sir ")
        break
