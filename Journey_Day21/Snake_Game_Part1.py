from turtle import Turtle,Screen
import time
from Snake_class import snakeobject
from FoodClass import Food
from ScoreBoard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome to the classic snake ladder game sir ")
screen.tracer(0)

f1=Food()
s1=snakeobject()
score=Scoreboard()

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

    #Now comes the part where we detect collision and do the aftermath
    if s1.segments[0].distance(f1)<15:
        f1.move_to_new_location()
        s1.extend()
        score.increase_score()

    if s1.segments[0].xcor()>290 or s1.segments[0].xcor()< -290 or s1.segments[0].ycor()>280 or s1.segments[0].ycor()<-280:
        score.game_over()
        game_is_on=False

    for seg in s1.segments[1:] :
        if s1.segments[0].distance(seg)<10:
            score.game_over()
            game_is_on=False



screen.exitonclick()
