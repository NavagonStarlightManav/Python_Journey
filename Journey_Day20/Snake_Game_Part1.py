from turtle import Turtle,Screen
import time
from Snake_class import snakeobject

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome to the classic snake ladder game sir ")
screen.tracer(0)

s1=snakeobject()

screen.listen()
screen.onkey(s1.move_up, "Up")
screen.onkey(s1.move_right, "Right")
screen.onkey(s1.move_down, "Down")
screen.onkey(s1.move_left, "Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    s1.move_forward()


screen.exitonclick()
