from turtle import Turtle,Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score of the game {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("Game over Honey", move=False, align='center', font=('Arial', 24, 'normal'))
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score of the game {self.score}", move=False, align='center', font=('Arial', 24, 'normal'))