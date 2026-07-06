from turtle import Turtle

starting_positions = [0,-20,-40]
class Console(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        
    def make_console(self,x_cor):
        for i in starting_positions:
            segment = Turtle("square")
            segment.penup()
            segment.goto(x_cor,i)
            self.segments.append(segment)
            
    def up(self):
        if self.ycor() < 300:
            self.forward(30)

    def down(self):
        if self.ycor() > -300:
            self.back(30)


