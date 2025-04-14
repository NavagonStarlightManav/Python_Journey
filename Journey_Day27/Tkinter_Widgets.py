from tkinter import *


window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20)


label = Label(text="Great_Learning")
label.config(text="Manav_Widgets")
label.pack()


def action():
    print(entry.get())

def action_2():
    print(text.get("1.0",END))
    # 1.0 Specifies the line from which to pick text and Go till end of Text

button = Button(text="Click Me", command=action)
button.pack()

entry=Entry(width=30)
entry.insert(END,string="Welcome to the Interface sir ")
entry.pack()

# using place instead of pack we can specify our coordinates

text=Text(height=5,width=30)
text.focus()
text.pack()


button_2 = Button(text="Submit Text", command=action_2)
button_2.pack()

def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar() # IntVar acts as bridge between  python codes and widgets and if button is checked returns 1 else 0
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# so the summary is : 1) We create appearence of widget in window
#                     2) then a function to get value from it
#                     3) Then a button is created to call the function
#                     4) finally widget is packed


def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used) # tkinter recognises any selection and function retrieves that values
listbox.pack()

# entry.insert(END, "Welcome to the Interface sir")
# Insert this text at the end of the entry box
# If the entry box was empty, it'll be added at the beginning If something already exists, this appends to the end

# <<ListboxSelect>> is an event in tkinter that means user has selected smth in list now

# grid command or place be used in such a way that no other system should be used

window.mainloop()