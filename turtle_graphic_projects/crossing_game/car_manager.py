from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            coord_y_random = random.randint(-260, 260)
            new_car.goto(320, coord_y_random)
            self.cars.append(new_car)

    def car_movement(self):
        for car in self.cars:
            car.backward(self.car_speed)
            if car.xcor() < -320:
                self.cars.remove(car)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

