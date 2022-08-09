from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.new_segrements = []
        self.score = 0
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.goto(0,270)
        self.write(f"score = {self.score}", True, align=ALIGNMENT, font = FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font = ("Arial", 24, "normal")
)

    #add new_square if it eats the food
    def increase_score(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()




        
