from tkinter import *

window = Tk()
window.minsize(width=600, height= 400)

label = Label(text= "hello", font= ("times new roman",24, "bold"), )
label.pack()

def button_opertion():
    label["text"] = input.get()

button = Button(text= "click me", command = button_opertion)
button.pack()

input = Entry(width= 10)
input.pack()

window.mainloop()