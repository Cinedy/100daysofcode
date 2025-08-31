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


def random_walk():
    randy.forward(10)
    randy.setheading(random.choice(degree))

randy = t.Turtle()
randy.speed(8)
randy.pensize(6)
for _ in range(50):
    random_walk()
    randy.color(random_color())



