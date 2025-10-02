from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.coord_x_velocity = 10
        self.coord_y_velocity = 10
        self.move_speed = 0.1

    def movement_ball(self):
        coord_x = self.xcor() + self.coord_x_velocity
        coord_y = self.ycor() + self.coord_y_velocity

        self.goto(coord_x,coord_y)

    def bounce_y(self):
        self.coord_y_velocity *= -1

    def bounce_x(self):
        self.coord_x_velocity *= -1
        self.move_speed *= 0.9

    def hit_ball(self):
        self.bounce_y()
        self.bounce_x()

    def ball_reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()






