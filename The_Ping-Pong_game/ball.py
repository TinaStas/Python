from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # if (self.xcor()>-390 and self.xcor()<390) and (self.ycor()>-290 and self.ycor()<290):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        #reverse the direction of y
        self.y_move *= -1

    def bounce_x(self):
    #reverse the direction of y
        self.x_move *= -1
        self.move_speed *= 0.9 #increase the speed after every hit --more challenging

    
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1


