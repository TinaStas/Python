from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
directions = [0,90,180,270]

timmy.speed(0)
timmy.pensize(15)   
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

for _ in range(200):
    timmy.pencolor(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()