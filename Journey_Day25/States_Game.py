from turtle import Turtle,Screen
import time
from States_Data import StatesData
import pandas as pd

dataset_2=pd.read_csv("50_states.csv")

screen = Screen()
screen.setup(width=700, height=700)
screen.bgpic("blank_states_img.gif")
screen.title("State Game")
screen.tracer(0)

stata_list=[]
state_count=0

state_missed=[]

while state_count !=50:
    time.sleep(0.5)
    screen.update()
    state_guess = screen.textinput("States Guess", "Enter state for Map :")
    if state_guess=="Exit":
        break
    else:
        stata_list.append(state_guess)
        s1 = StatesData(state_guess)
        s1.Move_to_position()
        state_count += 1

difference = [item for item in dataset_2.state.tolist() if item not in stata_list ]

remaining_dataset=pd.DataFrame(difference)
remaining_dataset.to_csv("remaining_states.csv",header=False)

screen.exitonclick()