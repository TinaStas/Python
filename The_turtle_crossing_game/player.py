from turtle import Turtle
import random 
from random import randint

COLORS = ['red','blue','yellow','green','brown','pink','orange']
MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE
        
    def create_car(self):
        # to decrease the number of cars created, let's assume that a car is created if the chance == 1
        chance = randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.goto(300,randint(-260,260))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
