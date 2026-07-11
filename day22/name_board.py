import turtle

class NameBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()

    def write_name(self,x_cordinate,y_cordinate,answer_state):

        self.goto(x_cordinate,y_cordinate)
        self.write(
        answer_state,
        font=("Courier", 13, "bold")
        )