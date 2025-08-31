import turtle as t
import random

t.colormode(255)

degree = 0, 90, 180, 270

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def spirograph(size_of_gap):   
    for _ in range(int(360 / size_of_gap)):
        randy.circle(100, None, None)
        randy.color(random_color())
        randy.setheading(randy.heading() + size_of_gap)

randy = t.Turtle()
randy.speed(11)
spirograph(5)

screen = t.Screen
screen.exitonclick()


