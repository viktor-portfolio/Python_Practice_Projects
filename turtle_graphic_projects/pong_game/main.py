from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player1 = Paddle(350)
player2 = Paddle(-350)
scoreboard = Scoreboard()
pong_ball = Ball()


screen.listen()
screen.onkey(player1.movement_up, "w")
screen.onkey(player1.movement_down, "s")

screen.onkey(player2.movement_up, "Up")
screen.onkey(player2.movement_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.movement_ball()

    if pong_ball.ycor() > 290 or pong_ball.ycor() < -290:
        pong_ball.bounce_y()

    #right paddle collision
    if pong_ball.xcor() > 320 and pong_ball.distance(player1) < 50:
        pong_ball.hit_ball()

    #left paddle collision
    if pong_ball.xcor() < -320 and pong_ball.distance(player2) < 50:
        pong_ball.hit_ball()

    #ball miss right side
    if pong_ball.xcor() > 380:
        pong_ball.ball_reset()
        scoreboard.left_point()

    #ball miss left side
    if pong_ball.xcor() < -380:
        pong_ball.ball_reset()
        scoreboard.right_point()

    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        game_is_on = False










screen.exitonclick()