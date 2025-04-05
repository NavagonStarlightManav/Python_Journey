from turtle import Turtle,Screen

STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class snakeobject:
    def __init__(self):
        self.segments = []
        for positions in STARTING_POSITIONS:
            self.new_turtle = Turtle()
            self.new_turtle.shape("square")
            self.new_turtle.color("white")
            self.new_turtle.penup()
            self.new_turtle.goto(positions)
            self.segments.append(self.new_turtle)

    def move_forward(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(UP)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(DOWN)

    def move_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(RIGHT)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(LEFT)
