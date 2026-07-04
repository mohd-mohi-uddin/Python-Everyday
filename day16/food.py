import random
import turtle

class Food:

    def __init__(self):
        self.food =turtle.Turtle("circle")
        self.food.color("orange")
        self.food.shapesize(0.5,0.5)
        self.food.penup()

    def make_food(self):
        """code for snake food"""
        x_cor = random.randrange(-260, 261, 20)
        y_cor = random.randrange(-260, 261, 20)
        self.food.goto(x_cor,y_cor)
