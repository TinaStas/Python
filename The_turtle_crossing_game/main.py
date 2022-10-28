from turtle import Screen, distance
from car import Car
from player import Player
from level import Level
import time
#configure screen settings

screen = Screen()
screen.setup(width = 600, height = 600)
# screen.bgcolor("bLack")
screen.title("My turtle crossing game!")
screen.tracer(0) #turn off the tracer

car = Car()
player = Player()
level = Level()

screen.listen()
screen.onkey(fun = player.move_forward , key= "Up")

is_game_On = True

while is_game_On:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

#collision with cars - game over

    for i in car.all_cars:
        if player.distance(i)<20:
            is_game_On = False
            level.game_over()

#collision with the wall - update level and start again and increase the speed of the cars (i.e spe*=0.09)

    if player.ycor()>280:
        level.increase_score()
        player.go_to_start()
        car.increase_speed()

screen.exitonclick()
