from turtle import Turtle
import turtle 

#Define our constants

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] 

    def create_snake(self): 
        """create the snake body -- 3 squares together"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        """create a new square and append it in the list of segments"""
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)  
        self.segments.append(new_square)

    def extend_snake(self):
        """add a new square in the tail"""
        self.add_segment(self.segments[-1].position())

    
    #define how the snake moves

    def moves(self):
        """Make the snake move"""
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.head.forward(MOVE_DISTANCE)


    #define snake's direction

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)






