from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=400, width=800)
screen.bgcolor('light yellow')
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(fun=player.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.3)
    screen.update()
    car.create_car()
    car.move_car()

    # detect when turtle collides with car
    for every_car in car.all_cars:
        if every_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect when player reached the other side
    if player.at_finish_line():
        player.go_to_start()
        car.speed_up()
        scoreboard.increase_score()

screen.exitonclick()