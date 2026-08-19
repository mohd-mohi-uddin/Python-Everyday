import turtle

timmy = turtle.Turtle()

timmy.speed(0)

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def move_clockwise():
    timmy.right(10)

def move_anticlockwise():
    timmy.left(10)

def clear():
    timmy.reset()
   
screen = turtle.Screen()
screen.listen()

screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(move_clockwise,"d")
screen.onkey(move_anticlockwise,"a")
screen.onkey(clear,"c")

screen.exitonclick() 