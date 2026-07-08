from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.updated_score()

    def updated_score(self):
        self.clear()
        self.score += 1
        self.write(
        f"LEVEL:{self.score}",
        font=("Courier", 24, "normal")
        )

    def gameover(self):
        self.goto(0,0)
        self.write(
        "Game Over!",
        align="center",
        font=("Courier", 25)
        )
        