import random as r
from turtle import Turtle

FOOD_POSITION = []

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.color("orange")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_cord = r.randint(-27, 27) * 10
        y_cord = r.randint(-27, 27) * 10
        self.goto(x_cord, y_cord)


