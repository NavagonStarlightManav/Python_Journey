from turtle import Turtle,Screen
FONT=("Ariel",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.update_scoreBoard()

    def update_scoreBoard(self):
         self.clear()
         self.goto(-280, 250)
         self.write(f"Level is {self.level} :", align="left", font=FONT)

    def increase_level(self):
         self.level+=1
         self.update_scoreBoard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over sir ", align="left", font=FONT)


