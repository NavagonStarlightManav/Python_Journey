from tkinter import *

window=Tk()
window.title("My First GUI Programs")
window.minsize(width=500,height=300)

my_label=Label(text="Love yea Nancy",font=("Arial",24,"bold"))
my_label.pack()

# Pack applies concept of default arguments, and we can just specify the arguments we want to change

my_label['text']="New Text"
my_label.config(text="New Text")

# Learning Buttons and Input

input=Entry(width=10)
input.pack()

def button_click():
    print("I Got The Internship sweety")
    my_label.config(text=input.get())

button=Button(text="Click Me",command=button_click)
button.pack()

window.mainloop()