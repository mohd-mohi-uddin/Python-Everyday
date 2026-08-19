from turtle import Turtle

starting_positions = [0,-20,-40]
class Paddle(Turtle):

    def __init__(self,paddle_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("olive drab")
        self.paddle_pos(paddle_pos)

    def paddle_pos(self,paddle_side):
        self.penup()
        self.goto(paddle_side,0)

    def up(self):
        if self.ycor() < 300:
            new_cor = self.ycor() + 50
            self.goto(self.xcor(),new_cor)

    def down(self):
        if self.ycor() > -300:
            new_cor = self.ycor() - 50
            self.goto(self.xcor(),new_cor)


