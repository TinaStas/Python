from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,cordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) #we need to be 20x20
        self.speed("fastest")
        self.penup()
        self.goto(cordinates) 

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(),new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(),new_ycor)

