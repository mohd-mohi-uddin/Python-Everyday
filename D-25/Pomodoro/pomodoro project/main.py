from tkinter import *
from pathlib import Path
import math
# ---------------------------- CONSTANTS ------------------------------- #
BASE_DIR = Path(__file__).parent
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label["text"]= "Timer"
    canvas.itemconfig(timer_count, text = "00:00")
    tickmark.config(text= "")

    global reps
    reps = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_button_function():
    global reps

    reps += 1
    work_time = WORK_MIN * 60
    rest_time = SHORT_BREAK_MIN*60
    last_rest = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(last_rest)
        title_label["text"] = "Break"
    elif reps % 2 == 0:
        count_down(rest_time)
        title_label["text"] = "Break"
    else:
        count_down(work_time)
        title_label["text"] = "Work"

def count_down(count):
    mins = count // 60
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_count,text= f"{mins}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_button_function()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        tickmark.config(text=mark)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")


tomato_image = PhotoImage(file= BASE_DIR /"tomato.png")
canvas = Canvas(width=200,height=224, bg= YELLOW, highlightthickness=0)
canvas.create_image(100,112,image= tomato_image)
timer_count = canvas.create_text(100,135, text="00:00", font=(FONT_NAME,35,"bold"), fill="white")
canvas.grid(column=1,row=1)

title_label = Label(text="Timer", font= (FONT_NAME,50,"bold"), fg = GREEN, bg= YELLOW)
title_label.grid(column=1, row= 0)

start_button = Button(text= "Start",highlightthickness=0, command= start_button_function)
start_button.grid(column=0,row=2)

reset_button = Button(text= "Reset",highlightthickness=0, command= reset_timer)
reset_button.grid(column=2,row=2)

tickmark = Label(font= (24), fg = "black", bg= YELLOW)
tickmark.grid(column=1, row= 3)

window.config(padx=100,pady=50,bg= YELLOW)
window.mainloop()