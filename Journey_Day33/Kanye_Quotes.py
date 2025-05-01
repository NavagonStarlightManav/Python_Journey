from tkinter import *
import requests


window=Tk()
window.title("Kanya  says : ")
window.config(padx=50,pady=50)

def get_quote():
    response=requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data=response.json()
    quote=data['quote']
    canvas.itemconfig(quote_text,text=quote)


canvas=Canvas(width=300,height=400)
background_img=PhotoImage(file="background.png")
canvas.create_image(150,207,image=background_img)
quote_text=canvas.create_text(150,207,text="Kanye Quote Goes Here",width=250,font=("Ariel",16,"bold italic"))
canvas.grid(row=0,column=0)

kanya_img=PhotoImage(file="kanye.png")
kanye_button=Button(image=kanya_img,highlightthickness=0,command=get_quote)
kanye_button.grid(row=1,column=0)

window.mainloop()