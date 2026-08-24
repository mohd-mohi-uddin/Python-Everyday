from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300,height=100)
window.config(padx=20,pady=30)

def kilometer_conversion():
    miles = input.get()
    kilometers = float(miles) * 1.60934
    label1["text"] = round(kilometers,1)

label = Label(text="is equal to", font = (24))
label.grid(column=0,row=1)

input = Entry(width= 15, justify= "center")
input.grid(column=1,row =0)

label0 = Label(text="Miles", font = (24))
label0.grid(column=2,row=0)

label1 = Label(text="0", font = (16))
label1.grid(column=1,row=1)

label2 = Label(text="Kilometers", font = (24))
label2.grid(column=2,row=1)

button = Button(text= "Calculate", command= kilometer_conversion)
button.grid(column= 1, row =2)

window.mainloop()