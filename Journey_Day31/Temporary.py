from tkinter import *
from tkinter import messagebox
import pyperclip
import json

window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas=Canvas(height=200,width=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


website_label=Label(text="Website")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username")
email_label.grid(rows=3,column=0)
password_label=Label(text="password")
password_label.grid(row=6,column=0)
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    new_data={
        website: {
            "email":email,
            "password":password,
        }

    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you havent left any fields empty")
    else:
          try:
              with open("data.json", "r") as data_file:
                  data = json.load(data_file)
          except FileNotFoundError:
              with open("data.json", "w") as data_file:
                  json.dump(new_data, data_file, indent=4)

          else:
              data.update(new_data)
              with open("data.json", "w") as data_file:
                  json.dump(data, data_file, indent=4)
          finally:
              website_entry.delete(0, END)
              password_entry.delete(0, END)


def password_generator():
    import random

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]

    password_letters=[random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols=[random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers=[random.choice(numbers) for _ in range(2,4)]

    password_list=password_numbers+password_symbols+password_letters
    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)

def search_credentials():
    website=website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title="Information",message=f"{data[website]['email']} \n {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops",message="Sorry sir There seems to be no file available")


website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
email_entry=Entry(width=35)
email_entry.grid(row=4,column=1,columnspan=2)
email_entry.insert(0,"ManavGoyal2006@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=6,column=1,columnspan=2)

generate_search_button=Button(text="Search Credentials",command=search_credentials)
generate_search_button.grid(row=1,column=3)

generate_password_button=Button(text="Generate PassWord",command=password_generator)
generate_password_button.grid(row=6,column=3)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=7,column=1,columnspan=2)
window.mainloop()