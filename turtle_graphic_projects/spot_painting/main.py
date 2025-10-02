import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()

tim.speed(50)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

def rows(radius, travel, row_count):
    for row in range(row_count):
        tim.color(random.choice(color_list))
        tim.penup()
        tim.begin_fill()
        tim.circle(radius)
        tim.end_fill()
        tim.forward(travel)


def painting(starting_pos = -100, coord_y = -200, gap_inbetween = 50, radius = 20, row_count = 10, column_count = 10):
    tim.hideturtle()
    tim.teleport(starting_pos, coord_y)
    for column in range(column_count):
        rows(radius,gap_inbetween,row_count)
        coord_y += gap_inbetween
        tim.teleport(starting_pos, coord_y)

painting()
screen.exitonclick()