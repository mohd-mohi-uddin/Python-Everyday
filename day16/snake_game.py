import turtle
import time
import random

"""gameover code"""
gameover_text = turtle.Turtle()
gameover_text.hideturtle()
gameover_text.color("white")

"""screen operations"""
screen = turtle.Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("The Snake Arcade")
screen.listen()
screen.tracer(0)

"""code for snake food"""
food = turtle.Turtle()
screen.tracer(0)
food.penup()
x_cor = random.randint(-260,260)
y_cor = random.randint(-260,260)
food.goto(x_cor,y_cor)
food.dot(10,"yellow")
food.hideturtle()
screen.update()


my_list = [0,-20,-40]
turtle_list= []

def make_turtle(x_value):
    """making a snake using three turtles"""
    timmy = turtle.Turtle()
    timmy.penup()
    timmy.speed("slowest")
    timmy.shape("square")
    timmy.color("white")
    timmy.goto(x = x_value,y = 0)
    return timmy

def move_right():
    """made for keyborad keys, to make snake turn right when d is pressed"""
    turtle_list[0].right(90)

def move_left():
    """made for keyborad keys, to make snake turn left when a is pressed"""
    turtle_list[0].left(90)

def snake_turn(heading,right,left):
    """function to make snake turn using keyboard"""
    if turtle_list[0].heading() == heading:
        screen.onkey(move_right,right)
        screen.onkey(move_left,left)

# screen.tracer(0)

for item in my_list: 
    new_turtle = make_turtle(item)
    turtle_list.append(new_turtle)

screen.update()

move = True
while move:

    if abs(turtle_list[0].xcor()) > 280 or abs(turtle_list[0].ycor()) > 280 :
        gameover_text.write(
        "Game Over!",
        align="center",
        font=("Courier", 25)
        )
        move = False


    screen.update()
    for i in range(len(my_list)-1,0,-1):
        turtle_list[i].goto(turtle_list[i-1].xcor(),turtle_list[i-1].ycor())
        time.sleep(0.1)
    turtle_list[0].forward(20)

    snake_turn(0,"s","w")
    snake_turn(90,"d","a")
    snake_turn(180,"w","s")
    snake_turn(270,"a","d")

screen.exitonclick()