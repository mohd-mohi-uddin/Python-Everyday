import turtle
import time
from snake import Snake
from food import Food
from scorecard import Scorecard

"""screen operations"""
screen = turtle.Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("The Snake Arcade")
screen.listen()
screen.colormode(255)
screen.tracer(0)

snake = Snake()
food = Food()
food.make_food()
scorecard = Scorecard()

screen.update()

"""function to make snake turn using keyboard"""
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")

move = True
while move:

    """if snake touches end of screen it dies"""
    if abs(snake.turtles[0].xcor()) > 280 or abs(snake.turtles[0].ycor()) > 280 :
        move = False
        scorecard.gameover_popup()
    
    """if snake touches its tail with head then it dies"""
    for segment in snake.turtles[1:]:
        if snake.turtles[0].distance(segment) < 10:
            move = False
            scorecard.gameover_popup()
        
    snake.move()
    time.sleep(0.24)
    screen.update()

    if snake.turtles[0].distance(food.food) < 15:
        snake.turtles.append(
            snake.make_segment(
            snake.turtles[-1].xcor(),
            snake.turtles[-1].ycor()
            )
            )
        food.make_food()

screen.exitonclick()