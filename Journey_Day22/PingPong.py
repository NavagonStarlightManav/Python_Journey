from turtle import Turtle , Screen
import time
from Paddles import Paddle
from Ping_ball import Ball
from scoreboard import scoreboard


screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=800)
screen.title("Welcome To The Classic PingPong Game ")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
b1=Ball()
s1=scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


while True:
    screen.update()
    time.sleep(b1.speed_current)
    b1.move()

    if b1.ycor()>360 or b1.ycor()<-360:
         b1.bounce()

    if b1.distance(r_paddle)<70 and b1.xcor()>340 or b1.distance(l_paddle)<70 and b1.xcor()<-340:
         b1.bounce_x()
         b1.speed()

    if b1.xcor()>365:
          b1.reset_coordinates()
          s1.l_point()

    if b1.xcor()<-365:
          b1.reset_coordinates()
          s1.r_point()


screen.exitonclick()