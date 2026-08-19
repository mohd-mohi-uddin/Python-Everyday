import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(car.increase_speed)

    car.create_car()
    car.move_cars()
   
   #collision with car

    if car.collision(player):
        scoreboard.gameover()
        game_is_on = False

    #scorecard
    if player.ycor() > 280:
        scoreboard.updated_score()
        car.increase_speed *= 0.5
        player.refresh()

screen.exitonclick()
