from turtle import Turtle, Screen, color
import random

screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle will win the race? Enter a colour:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#create a list of different turtles
all_turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    color_selected = random.choice(colors)
    new_turtle.color(color_selected)
    colors.remove(color_selected)
    new_turtle.penup()
    #the width of the turtle is 40. So we should start from the position x=250-(40/2)=230
    new_turtle.goto(-230,-100 + 30*i) #alternatively we can define a y=[-70,-40,-10,20,50,80]
    new_turtle.down()
    all_turtles.append(new_turtle)

end = False
while not end:
    for i in range(6):
        tur = all_turtles[i]
        tur.penup()
        tur.forward(random.randint(0,10))
        tur.pendown()
        if tur.xcor() > 230:
            if tur.pencolor() != user_bet:
                print(f"You lose. The {tur.pencolor()} turtle won.")
            else:
                print(f"You won! The {user_bet} turtle is the winner.")
            end = True
screen.exitonclick()