from tkinter import *

window=Tk()
window.title("Miles Converter Project")
window.minsize(width=500,height=300)

my_label=Label(text="Miles",font=("Arial",14,"bold"))
my_label.grid(column=0,row=0)

def calculate():
    answer=float(input.get())*1.60934
    result_label.config(text=f"{answer}")


input=Entry(width=10)
input.grid(column=3,row=0)

new_label=Label(text="is equal to",font=("Arial",14,"bold"))
new_label.grid(column=0,row=4)

km_label=Label(text="km",font=("Arial",14,"bold"))
km_label.grid(column=4,row=4)

result_label=Label(text="0",font=("Arial",14,"bold"))
result_label.grid(column=3,row=4)


button=Button(text="Calculate",command=calculate)
button.grid(column=3,row=5)


window.mainloop()
