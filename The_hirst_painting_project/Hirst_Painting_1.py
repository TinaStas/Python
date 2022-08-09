# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
# list_of_colors = []
# for i in range(0, len(colors)-1):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     new_color = (r, g, b)
#     list_of_colors.append(new_color)
#
# print(list_of_colors)
import random
from turtle import Turtle, Screen, colormode

colormode(255)
color_list = [(159, 153, 149), (125, 104, 87), (213, 211, 207), (168, 159, 162),
              (53, 25, 11), (10, 28, 50), (157, 167, 177), (131, 79, 91), (155, 170, 161), (65, 100, 121), (62, 15, 24),
              (16, 40, 25), (73, 111, 88), (156, 141, 70), (125, 26, 38), (200, 195, 173),
              (127, 34, 19), (166, 103, 117), (145, 119, 115), (200, 186, 190), (90, 76, 18), (35, 83, 47),
              (35, 59, 102), (100, 145, 123), (205, 185, 182)]

screen = Screen()
timmy = Turtle()

timmy.hideturtle()
timmy.speed("fastest")

#make all dots appear 
timmy.penup()
timmy.setheading(220)
timmy.forward(350)
timmy.setheading(0)
timmy.pendown()

def turn_left():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(50)

def turn_right():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)
    timmy.forward(50)

for i in range(10):
    
    for _ in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)    
        timmy.pendown()
    timmy.penup()

    if i%2==0:
        turn_left()
    else:
        turn_right()

    timmy.pendown()


screen.exitonclick()