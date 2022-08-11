from turtle import Turtle

FONTS = ('Courier', 80, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_r = 0
        self.score_l = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.score_r}", align="right", font = FONTS)
        self.goto(100,200)
        self.write(f"{self.score_l}", align="left", font = FONTS)

    def increase_score_l(self):
        self.score_l += 1
        self.update_score()
    
    def increase_score_r(self):
        self.score_r += 1
        self.update_score()