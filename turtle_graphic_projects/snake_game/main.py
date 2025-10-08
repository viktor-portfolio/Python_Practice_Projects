import time
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset_snake()

    for segment in snake.segments[1:]: #gives everything other than the first element same as len(snake.segments)
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset_snake()




screen.exitonclick()