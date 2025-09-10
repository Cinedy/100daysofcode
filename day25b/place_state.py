# Place state on map
 
from turtle import Turtle

class PlaceState(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(state, move=False, align="center", font="Arial")


