#import colorgram
import turtle as t
import random

# color_list = []

# colors = colorgram.extract('hirst_spot.jpeg', 20)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     color_list.append(new_color)

color_list = [(208, 165, 124), (248, 235, 237), (140, 49, 106), (164, 169, 38), (245, 79, 56), (215, 233, 230), (234, 112, 164), (3, 142, 51), (241, 65, 139), (1, 143, 185), (162, 56, 52), (49, 202, 226), (19, 165, 126), (254, 230, 0), (240, 220, 59), (216, 236, 240), (28, 198, 220), (137, 181, 155), (218, 176, 192)]

t.colormode(255)
tim = t.Turtle()

tim.speed(8)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)

for _ in range (10):
    for _ in range (10):
        tim.fd(50); tim.dot(20, random.choice(color_list)); tim.fd(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(1000)
    tim.setheading(0)


screen = t.Screen()
screen.exitonclick()