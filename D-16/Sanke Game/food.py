import random
import turtle

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.penup()
        self.reset_food()

    def reset_food(self):
        """code for snake food"""
        x_cor = random.randrange(-260, 261, 20)
        y_cor = random.randrange(-260, 261, 20)
        self.goto(x_cor,y_cor)
