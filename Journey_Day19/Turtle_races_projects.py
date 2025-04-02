import random
import turtle
from turtle import Turtle , Screen
tim =Turtle()
screen=Screen()
screen.setup(width=500,height=400)

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

is_race_on=True

def move_forwards(tim):
    tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

turtle_heading=170

user_bet=screen.textinput(title="Make your bet",prompt="Please choose the color which you will win")
x=-180
y=0
index=0
turtle_list=[]

for turtles in range(1,8):
    turtle_object=Turtle()
    turtle_object.color(rainbow_colors[index])
    turtle_object.goto(x,y)
    turtle_object.setheading(0)
    turtle_object.speed(random.randint(1,10))
    turtle_list.append(turtle_object)
    y+=30
    index+=1

if user_bet:
    is_race_on=True

while is_race_on:
    for turtles in turtle_list:
        if turtles.xcor()>180:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You have won with the color {winning_color}")
            else:
                print("sorry sir you have lost ")
        else:
            turtles.forward(random.randint(1,20))


screen.exitonclick()





