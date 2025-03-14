print(r''' 
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/''')

print("Welcome to Treasure Island\nYour Mission is to find the treasure")

direction=input("Please choose your direction sir : Left or Right").lower()
if direction=="Right":
    print("Sorry Sir but chose wrong direction I will have to ask you to leave")

elif direction=="left":
    print("Going Good Enough Sir ")
    Swim_Wait=input("You wanna Swim or Wait sir ?  ")
    if Swim_Wait=="Swim":
        print("Sorry sir better luck next time ")
    else:
        door_colour=input("Which colour door you wannna give ? blue , red , yellow ")
        if door_colour=="blue" or door_colour=="red":
            print("Sorry Sir you have to try again ")
        else:
            print("You win the game sir Congratulations ")
else:
    print("Please enter correct direction sir")

# An important major concept is that backslash can be used for escape symbol or that we dont want that symbol to be used it is just part of string
print(' Please enter the your opinion \'Please be \\n Optimistic or passimistic\' ')

