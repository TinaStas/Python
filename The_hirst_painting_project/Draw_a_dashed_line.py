# Draw a dashed line

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("arrow")

for _ in range(21):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)    
    timmy.pendown()

screen = Screen()
screen.exitonclick()