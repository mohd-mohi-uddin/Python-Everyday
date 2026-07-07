from turtle import Turtle , Screen
from designs import Midline, MakeCircle
from console import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen = Screen() 
screen.setup(width = 1100,height = 700)
screen.bgcolor("yellow green")
screen.tracer(0)

midline = Midline()
centrecircle = MakeCircle()
ball = Ball()
scorecard = Scorecard()

right_paddle = Paddle(525)
left_paddle = Paddle(-525)

screen.listen()
screen.onkeypress(right_paddle.up,"Up")
screen.onkeypress(right_paddle.down,"Down")
screen.onkeypress(left_paddle.up,"w")
screen.onkeypress(left_paddle.down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.increase_speed)

    ball.move()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 500 or ball.distance(left_paddle) < 50 and ball.xcor() < -500:
        ball.bounce_x()

    if ball.xcor() > 530:
        ball.refresh()
        scorecard.l_point()
    
    if ball.xcor() < -530:
        ball.refresh()
        scorecard.r_point()

screen.exitonclick()