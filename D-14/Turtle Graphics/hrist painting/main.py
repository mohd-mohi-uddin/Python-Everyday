import turtle
import random
"""for extracting colors from image using color gram"""
# import colorgram


# list_of_colors = []
# colors = colorgram.extract('Python-Everyday/day14/hrist painting/hristimage.jpg',15)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     list_of_colors.append(new_color)
# print(list_of_colors)
turtle.colormode(255)

list_of_colors = [(99, 234, 231), (234, 99, 232), (236, 35, 108), (221, 231, 99), (145, 28, 66), (0, 99, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91)]

timmy = turtle.Turtle()

timmy.hideturtle()
timmy.penup()
timmy.speed(0)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for i in range(10):
    for _ in range(10):
        timmy.dot(15,random.choice(list_of_colors))
        timmy.forward(50)

    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.setheading(0)

screen = turtle.Screen() 
screen.exitonclick()