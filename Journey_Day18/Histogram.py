import turtle as t
from turtle import Turtle,Screen
import random

tim=t.Turtle()
tim.shape("turtle")
# import colorgram
# colors=colorgram.extract('image.jpeg',8)
#
# list_of_colour=[]
#
# for colours in colors:
#     r=colours.rgb.r
#     g=colours.rgb.g
#     b=colours.rgb.b
#     new_color=(r,g,b)
#     list_of_colour.append(new_color)

t.colormode(255)

image_colours=[(229, 228, 227), (226, 224, 225), (198, 175, 119), (125, 36, 23), (187, 157, 50), (170, 104, 56), (5, 56, 83), (201, 216, 205)]

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.pendown()


for rows in range(1,12):
    if rows%2!=0:
        turn=180
    else:
        turn=0
    for columns in range(1,12):
        tim.dot(20, random.choice(image_colours))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.pendown()
    tim.setheading(turn)

screen=Screen()
screen.exitonclick()