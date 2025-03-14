print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))
bill = 0;

if height >= 120:
    print("you are eligible for rollercoaster")
    age=int(input("Sir What's your  age sir ? "))
    if age<=12:
        print("Tickets gonna cost $5 each ")
        bill = 5
    elif age>12 & age<=18:
        print("Tickets gonna cost $10 each")
        bill =10
    else:
        print("Tickets gonna cost $15 each")
        bill =15

    Photoshoot = input("You wanna have Photoshoot too sir ? True/False ")
    if Photoshoot :
            bill+=5
            print(f" So the final bill is {bill}")
# multiple if are also used to check atleast once all the conditions are checked inspite of one condition being satisfied and exiting the checking process
else:
    print("We will have excuse you sir ")




number_to_check=int(input("What number you wanna check ? "))

if number_to_check % 2 ==0:
    print("Your number is even")
else:
    print("The number is odd")
print("\n\n")




print("Welcome to our Pizza store\nHave a look on our  carefully customer centric_"
      "Menu\nSmall pizza (s):$15 \nMedium pizza(m):$20 \nLarge pizza(L):$25\nExtra Pepperoni charges for small pizza:$2_"
      "\nExtra Pepperoni for Large Pizza: $3\nExtra cheese on Pizza : $5")

Pizza_size = input("Please select the portion sir : ")
Pepperoni=input("Sir Do you want extra pepperoni ? Yes or No")
Extra_Cheese=input("Sir Do you want extra Cheese ? Yes or No")
bill=0

if Pizza_size=="S":
    bill=15
elif Pizza_size=="M":
    bill=20
elif Pizza_size=="L":
    bill=25
    if Pizza_size==("S" or "M") and Pepperoni=="Yes" and Extra_Cheese=="Yes":
        bill+=7
    elif (Pizza_size=="S" or "M") and Pepperoni=="Yes" and Extra_Cheese=="No":
        bill+=2
    elif (Pizza_size=="S" or "M") and Pepperoni=="No" and Extra_Cheese=="Yes":
        bill+=5
    elif (Pizza_size=="S" or "M") and Pepperoni=="No" and Extra_Cheese=="No":
        bill+=0
    elif (Pizza_size == "L") and Pepperoni == "Yes" and Extra_Cheese == "Yes":
        bill += 8
    elif (Pizza_size == "L") and Pepperoni == "Yes" and Extra_Cheese == "No":
        bill += 3
    elif (Pizza_size == "L") and Pepperoni == "No" and Extra_Cheese == "Yes":
        bill += 5
    else:
        bill+=0
else:
    print("Please Select the right input sir ")

print("Your total bill will be $"+str(bill))




