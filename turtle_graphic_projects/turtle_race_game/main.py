from turtle import Turtle, Screen
import random

screen = Screen()

"""TURTLE RACE"""
screen.setup(500,400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter the color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_gang = []
coord_y = -70
is_race_on = False

for turtle_index in range(0,6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    coord_y += 30
    new_turtle.goto(-230, coord_y)
    turtle_gang.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_gang:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()

            if winner_color == user_bet:
                print(f"Your {winner_color} turtle won the race")
            else:
                print(f"You lost, the {winner_color} turtle won the race")

        random_movement_speed = random.randint(0, 10)
        turtle.forward(random_movement_speed)


screen.exitonclick()