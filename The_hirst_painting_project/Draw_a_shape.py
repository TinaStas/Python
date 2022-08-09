from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")

# # change color - create pentagon - agle=72
def draw_shape(angle):
    timmy.right(angle)
    timmy.forward(100)

#360:i=3,4,5,6,7,...10
color_list = ['red','blue','yellow','green','blueviolet','brown','pink','black','orange','grey']
for sides_num in range(3,11):
    timmy.color(random.choice(color_list))
    angle = 360 / sides_num
    for _ in range(sides_num):
        draw_shape(angle)

screen = Screen()
screen.exitonclick()
