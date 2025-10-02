from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position_x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position_x, 0)

    def movement_up(self):
        coord_y = self.ycor() + 40
        self.goto(self.xcor(), coord_y)

    def movement_down(self):
        coord_y = self.ycor() - 20
        self.goto(self.xcor(), coord_y)