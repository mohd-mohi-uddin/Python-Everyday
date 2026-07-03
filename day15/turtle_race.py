import turtle
import random

screen = turtle.Screen()
screen.setup(width = 500,height = 400)
user_choice = screen.textinput(title= "make your bet",prompt= "which turtle will win the race? select a clolr:")
y_cordinates = [74,45,15,-15,-45,-75]
colors = ["red","blue","green","yellow","orange","skyblue"]
all_timmy = []

for i in range(6):
    timmy = turtle.Turtle(shape = "turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(x=-230,y =y_cordinates[i])
    all_timmy.append(timmy)


move = True
while move:
    for turtles in all_timmy:
        
        if turtles.xcor() > 230:
            move = False
            winning_turtle = turtles.pencolor()
            if user_choice == winning_turtle:
                print("you won")
            else:
                print("you lose")


        turtles.forward(random.randint(0,10))

screen.exitonclick()
