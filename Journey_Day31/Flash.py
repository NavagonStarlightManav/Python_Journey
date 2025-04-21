from audioop import cross

import pandas
import pandas as pd
from pandas import read_csv
import random
current_card={}

try:
    df = read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=df.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    print(current_card["French"])
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    flip_timer=window.after(3000, func=flip_card)




def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_image)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data=pd.DataFrame(to_learn)
    data.to_csv("Words_to_learn.csv",index=False)


from tkinter import *
BACKGROUND_COLOR="#B1DDC6"

window=Tk()
window.title("Flash Capstone Project")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)

canvas=Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front=PhotoImage(file="card_front.png")
card_back_image=PhotoImage(file="card_back.png")
card_background=canvas.create_image(400,263,image=card_front)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",40,"italic"))
canvas.grid(row=0,column=0,columnspan=2)

cross_image=PhotoImage(file="wrong.png")
unknown_button=Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

check_image=PhotoImage(file="right.png")
known_button=Button(image=check_image,highlightthickness=0,command=is_known)

known_button.grid(row=1,column=1)

next_card()

window.mainloop()
