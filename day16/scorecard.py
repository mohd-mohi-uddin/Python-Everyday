import turtle
from pathlib import Path

BASE_DIR = Path(__file__).parent

class Scorecard(turtle.Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open(BASE_DIR/"data.txt") as data:
            self.highscore = int(data.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-280,270)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(
        f"Score: {self.score} High score: {self.highscore}",
        align="left",
        font=("Courier", 15)
        )

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(BASE_DIR/"data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.update_score()



    
    
