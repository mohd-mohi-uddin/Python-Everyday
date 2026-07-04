import turtle

class Scorecard:

    def __init__(self):
        self.gameover_text = turtle.Turtle()
        self.gameover_text.hideturtle()
        self.gameover_text.color("white")

    def gameover_popup(self):
        self.gameover_text.write(
        "Game Over!",
        align="center",
        font=("Courier", 25)
        )
    
    
