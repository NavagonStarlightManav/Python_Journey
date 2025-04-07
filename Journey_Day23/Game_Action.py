from turtle import Turtle , Screen

import scoreboard
from Cars_Class import Cars
import time
from player import Player

screen=Screen()
screen.setup(width=600,height=600)
screen.title("Welcome to Turtle Capstone Project")
screen.bgcolor("white")
screen.tracer(0)


c1=Cars()
p1=Player()
s1=scoreboard.Scoreboard()

screen.listen()
screen.onkey(p1.go_up,"Up")
game_is_on=True

while game_is_on:
    time.sleep(0.2)
    screen.update()

    c1.create_car()
    c1.move_cars()

    # Detect Collision With car
    for cars in c1.Car_segment:
        if cars.distance(p1)<30:
            s1.game_over()
            game_is_on=False

    # Detect collision with wall
    if p1.is_finish_line():
        c1.level_up()
        s1.increase_level()
        p1.go_to_start()




screen.exitonclick()
