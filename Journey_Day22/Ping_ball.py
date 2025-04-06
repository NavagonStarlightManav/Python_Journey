from turtle import Turtle,Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor=10
        self.y_cor=10
        self.speed_current=0.1

    def move(self):
        new_x=self.xcor()+self.x_cor
        new_y=self.ycor()+self.y_cor
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_cor*=-1
    def bounce_x(self):
        self.x_cor*=-1
        self.speed_current*=0.9

    def reset_coordinates(self):
        self.goto(0,0)
        self.speed_current=0.1
        self.bounce_x()




