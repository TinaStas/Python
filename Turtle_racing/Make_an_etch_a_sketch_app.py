from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(10)

def move_clockwise():
    tim.right(10)

def clear_drawing():
    tim.reset()

screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=move_counter_clockwise)
screen.onkey(key="D", fun=move_clockwise)
screen.onkey(key="C", fun=clear_drawing)

screen.exitonclick()