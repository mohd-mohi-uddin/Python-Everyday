import turtle
from turtle import Turtle
from turtle import Screen
import random

turtle.colormode(255)

timmy = Turtle()
timmy.shape("turtle")


"""making a random path"""
angles = [0,90,180,270]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

move = True
while move:
    timmy.pensize(10)
    timmy.speed(15)
    timmy.color(random_color())
    direction = random.choice(angles)
    timmy.setheading(direction)
    timmy.forward(30)   


# """drwaing a spirograph"""
# for _ in range(75):
#     timmy.speed(0)
#     timmy.color("green")
#     timmy.circle(100)
#     timmy.right(5)


# """making traingle to hexagon with different colors"""
# def draw_Shape(number_of_sides):
#     angle = 360/number_of_sides
#     timmy.color("green")
#     for j in range(number_of_sides):
#         timmy.forward(100)
#         timmy.right(angle)


# n=3
# for i in range(10):
#     draw_Shape(n)

#     n += 1
# # for i in range(3,11):
# #     draw_Shape(i)

# """making doted path"""
# # for i in range(10):
# #     timmy.pendown()
# #     timmy.forward(10)

# #     timmy.penup()
#     timmy.forward(10)


screen = Screen()
screen.exitonclick()

    
