from tkinter import *
from pathlib import Path
import pandas
import random
BASE_DIR= Path(__file__).parent

current_card = {}
to_learn = {}

#........................................CSV FILE HANDLING..........................................#
try:
    new_file = pandas.read_csv(BASE_DIR /"data"/"words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv(BASE_DIR /"data"/"telugu_to_english.csv")
    to_learn = original_file.to_dict(orient="records")
else:
    to_learn = new_file.to_dict(orient="records")
#...........................................CHANGE_CARD.............................................#
def next_card():
    global current_card
    global timer
    
    window.after_cancel(timer)
    timer= window.after(5000,flip_card)
    current_card = random.choice(to_learn)
    telugu_word = current_card["telugu"]
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(title_label, text="Telugu",fill= "black")
    canvas.itemconfig(word_label, text=telugu_word, fill= "black")

#............................................FLIP CARD...............................................#
def flip_card():
    canvas.itemconfig(canvas_image, image= new_image)
    canvas.itemconfig(title_label, text= "English",fill= "white")
    canvas.itemconfig(word_label, text= current_card["english"],fill= "white")

#Removing items which are guessed righ and moving them to csv.
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(BASE_DIR /"data"/"words_to_learn.csv",index= False)
    next_card()
    
#.............................................UI CODE................................................#

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

timer= window.after(5000,flip_card)

old_image = PhotoImage(file=BASE_DIR /"images"/"card_front.png")
new_image = PhotoImage(file=BASE_DIR /"images"/"card_back.png")
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image= canvas.create_image(400,263,image= old_image)
canvas.grid(column=0,row=0,columnspan=2)
title_label= canvas.create_text(400,180,text="Title",font=("Ariel",40,"italic"),)
word_label= canvas.create_text(400,300,text="word",font=("Nirmala UI",60,"bold"))

next_card()

#buttons
right_button_image = PhotoImage(file=BASE_DIR /"images"/"right.png")
right_button = Button(image=right_button_image,bd=0,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

wrong_button_image = PhotoImage(file=BASE_DIR /"images"/"wrong.png")
wrong_button = Button(image=wrong_button_image,bd=0,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)


window.mainloop()