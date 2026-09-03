from tkinter import *
from pathlib import Path
from quiz_brain import QuizBrain

BASE_DIR = Path(__file__).parent

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text="Score:0",bg=THEME_COLOR,fg="white")
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="text goes here",font= ("Arial",20,"italic"),width=280)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        right_image = PhotoImage(file=BASE_DIR /"images"/"true.png")
        self.right_button = Button(image=right_image,highlightthickness=0,bd=0,command=self.true_pressed)
        self.right_button.grid(column=1,row=2)

        wrong_image = PhotoImage(file=BASE_DIR /"images"/"false.png")
        self.wrong_button = Button(image=wrong_image,highlightthickness=0,bd=0,command=self.false_pressed)
        self.wrong_button.grid(column=0,row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text= "the questions has ended")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)