import turtle
import random


class Snake:

    def __init__(self):
        self.turtles = []
        self.segments()

    starting_positions = [0,-20,-40]

    def segments(self):
        for item in self.starting_positions: 
            new_turtle = self.make_segment(item,0)
            self.turtles.append(new_turtle)

    def make_segment(self,x_value,y_value):
        """making a snake using three turtles"""
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.speed("slowest")
        timmy.shape("square")
        random_color = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
        timmy.color(random_color)
        timmy.goto(x = x_value,y = y_value)
        return timmy
    
    def up(self):
        self.turtles[0].setheading(90)

    def down(self):
        self.turtles[0].setheading(270)

    def right(self):
        self.turtles[0].setheading(0)

    def left(self):
        self.turtles[0].setheading(180)

    def move(self):
        for i in range(len(self.turtles)-1,0,-1):
            self.turtles[i].goto(self.turtles[i-1].xcor(),self.turtles[i-1].ycor())
        self.turtles[0].forward(20)