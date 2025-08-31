
from turtle import Turtle, Screen
import random

timmy = Turtle()
colors = ["gray", "red", "orange", "gold", "green","violet", "purple", "slateblue", "blue", "lightblue"]

def paint(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        timmy.forward(100)
        timmy.right(angle)

for shape in range(3, 11):
    timmy.color(random.choice(colors))
    paint(shape)

screen = Screen()
screen.exitonclick()