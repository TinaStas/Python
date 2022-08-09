from turtle import Turtle, Screen

#Draw a square

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("arrow")

def draw_square():
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(120)

    # i = 0
    # while i<4:
    #     draw_square()
    #     i += 1

for _ in range(4):
    draw_square()

screen = Screen()
screen.exitonclick()