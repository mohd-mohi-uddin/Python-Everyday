import turtle

class Midline(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.make_mid_line()

    def make_mid_line(self):
        self.hideturtle()
        self.penup()
        self.goto(0,350)
        self.setheading(270)
        self.pensize(5)
        self.pencolor("olive drab")
        for i in range(36):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(15)
    
class MakeCircle(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.make_circle()

    def make_circle(self):
        self.penup()
        self.hideturtle()
        self.goto(0,-42)
        self.pendown()
        self.pencolor("olive drab")
        self.pensize(5)
        self.circle(50, steps= 5000)


        
        


