from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

timmy.speed(0)
colormode(255)

def draw_sprirograpg(angle):
    for _ in range(360//angle):
        timmy.pencolor(random_color())
        timmy.left(angle)
        timmy.circle(100)

draw_sprirograpg(5)    

screen = Screen()
screen.exitonclick()