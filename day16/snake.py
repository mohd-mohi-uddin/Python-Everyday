import turtle
import random

STARTING_POSITIONS = [0,-20,-40]
class Snake:

    def __init__(self):
        self.blocks = []
        self.segments()
        self.head = self.blocks[0]

    def segments(self):
        """make turtle using make_segment and
        add them to starting positons using goto() and 
        then save them in self.blocks list"""

        for item in STARTING_POSITIONS: 
            new_turtle = self.make_segment(item,0)
            self.blocks.append(new_turtle)

    def make_segment(self,x_value,y_value):
        """making a turtle using make snake body"""
        snake_body = turtle.Turtle()
        snake_body.penup()
        snake_body.speed("slowest")
        snake_body.shape("square")
        random_color = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
        snake_body.color(random_color)
        snake_body.goto(x = x_value,y = y_value)
        return snake_body
    
    def up(self):
        if self.blocks[0].heading() != 270:
            self.blocks[0].setheading(90)

    def down(self):
        if self.blocks[0].heading() != 90:
            self.blocks[0].setheading(270)

    def right(self):
        if self.blocks[0].heading() != 180:
            self.blocks[0].setheading(0)

    def left(self):
        if self.blocks[0].heading() != 0:
            self.blocks[0].setheading(180)

    def move(self):
        for i in range(len(self.blocks)-1,0,-1):
            self.blocks[i].goto(
                self.blocks[i-1].xcor(),
                self.blocks[i-1].ycor()
                )
        self.blocks[0].forward(20)

    def grow(self):
        self.blocks.append(
        self.make_segment(
        self.blocks[-1].xcor(),
        self.blocks[-1].ycor()
        )
        )

    def wall_collision(self):
        return abs(self.head.xcor()) > 280 or abs(self.head.ycor()) > 280
    
    def tail_collision(self):
            return self.head.distance(self.segment) < 10
          
        