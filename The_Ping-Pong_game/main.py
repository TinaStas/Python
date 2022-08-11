from turtle import Screen
from line import Line
from paddle import Paddle
from ball import Ball
from score import Score
import time

#configure screen settings

screen = Screen()

screen.setup(width = 800, height = 600)
screen.bgcolor("bLack")
screen.title("My pong game!")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
line = Line()
ball = Ball()
score = Score()

screen.listen()

#MOVE THE PADDLES

#CREATE COMMANDS FOR THE LEFT PADDLE
screen.onkey(fun = l_paddle.go_up, key="w")
screen.onkey(fun = l_paddle.go_down, key="s")

#CREATE COMMANDS FOR THE RIGHT PADDLE
screen.onkey(fun = r_paddle.go_up, key="Up")
screen.onkey(fun = r_paddle.go_down, key="Down")

is_gameOn = True

while is_gameOn:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()
        
    #detect collision with paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>320) or (ball.distance(l_paddle)<50 and ball.xcor()<-320):
        ball.bounce_x()
    
    #detect when paddle misses the ball
    if ball.distance(r_paddle)>50 and ball.xcor()>380:
        score.increase_score_r()
        ball.reset_position()

    if ball.distance(l_paddle)>50 and ball.xcor()<-380:
        score.increase_score_l()
        ball.reset_position()
        


screen.exitonclick()