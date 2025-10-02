import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player1.movement, 'space')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_movement()

    for car in car_manager.cars:
        if car.distance(player1) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player1.is_at_the_finish_line():
        player1.player_reset()
        scoreboard.increase_level()
        car_manager.level_up()


screen.exitonclick()