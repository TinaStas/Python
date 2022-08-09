from turtle import Screen
from scoreboard import Score
from snake import Snake
from food import Food
import time
from random import randint

#configure screen settings

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("bLack")
screen.title("My snake game!")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
#define keyboard symbols to tell the snake where to move

screen.listen()
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)

#play the snake game

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.moves()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.new_location()
        #create a scoreboard - increase the tail and score by one
        snake.extend_snake()
        score.increase_score()
       

    #detect collision with the wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_over = True
        score.game_over()

    # #detect collision with the tail
    for segment in snake.segments[1:]: 
        if snake.head.distance(segment) < 10:
            game_over = True
            score.game_over()


screen.exitonclick()



