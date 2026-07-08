from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():

    def __init__(self):
        self.car_list = []
        self.increase_speed = 0.1

    def create_car(self):
        random_choice = random.randint(1,6)
        if random_choice == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            random_y = random.randint(-250,250)
            car.goto(300,random_y)
            self.car_list.append(car)

    def move_cars(self):
        for cars in self.car_list:
            cars.backward(5)

    def collision(self,player):
        for i in self.car_list:
            if i.distance(player) < 20:
                return True
        return False


    
