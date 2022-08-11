from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,300)
        self.right(90)
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.draw_line()

    def draw_line(self):
        distance = int(round(self.distance((0,-300)),0))
        for _ in range(distance):
            self.forward(10)
            self.penup()
            self.forward(10)    
            self.pendown()