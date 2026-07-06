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

"""objects made using classes"""

snake = Snake()
food = Food()
scorecard = Scorecard()

screen.update()

"""function to make snake turn using keyboard"""

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.right,"d")
screen.onkey(snake.left,"a")

game_is_on = True
while game_is_on:

    """if snake touches end of screen it dies"""
    if snake.wall_collision():
        game_is_on = False
        scorecard.gameover_popup()
    
    """if snake touches its tail with head then it dies"""
    for snake.segment in snake.blocks[1:]:
        if snake.tail_collision():
            game_is_on = False
            scorecard.gameover_popup()
        
    snake.move()
    time.sleep(0.1)
    screen.update()

    if snake.head.distance(food) < 15:
        snake.grow()
        food.reset_food()

screen.exitonclick()