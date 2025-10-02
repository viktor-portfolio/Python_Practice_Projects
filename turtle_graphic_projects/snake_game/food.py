from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.refresh()


    def refresh(self):
        food_location_x = random.randint(-280,280) #you can create local variable inside the class to use in the innit
        food_location_y = random.randint(-280, 280)
        self.teleport(food_location_x, food_location_y)