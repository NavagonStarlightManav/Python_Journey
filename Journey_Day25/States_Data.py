import pandas as pd
from turtle import Turtle,Screen

dataset=pd.read_csv("50_states.csv")

class StatesData(Turtle):
    def __init__(self,state_guessed):
        super().__init__()
        self.y = 0
        self.x = 0
        self.row = dataset[dataset['state']== state_guessed]

    def Move_to_position(self):
        self.color("black")
        self.hideturtle()
        self.penup()
        self.x=self.row['x'].values[0]
        self.y=self.row['y'].values[0]
        self.goto(self.x,self.y)
        self.write(f"{self.row['state'].values[0]}", move=False, align="left", font=("Arial", 15, "normal"))





