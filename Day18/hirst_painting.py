# import colorgram
import random
import turtle as t

turtle = t.Turtle()
screen = t.Screen()
screen.setup(width=500, height=500)
t.colormode(255)
# colors = colorgram.extract('image.jpg', 30)
#
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r,g,b))
#
# print(color_list)


colors_lists = [(241, 253, 246), (243, 247, 253), (240, 231, 56), (221, 154, 74), (185, 64, 30), (239, 42, 120),
                (191, 12, 32), (35, 96, 173), (45, 213, 79), (20, 24, 54), (37, 35, 156), (234, 228, 4), (87, 185, 220),
                (220, 163, 10), (205, 12, 6), (196, 37, 78), (49, 25, 15), (74, 12, 47), (233, 58, 37), (26, 144, 31),
                (84, 236, 176), (80, 211, 144), (219, 138, 183), (12, 200, 218), (95, 75, 12), (241, 157, 197),
                (75, 80, 217), (11, 36, 28)]

turtle.speed("fastest")
turtle.penup()
turtle.goto(x=-230, y=-230)

while True:
    turtle.dot(20, random.choice(colors_lists))
    if turtle.xcor() > 250:
        turtle.goto(x=-230.0, y=turtle.ycor() + 50)
    else:
        turtle.forward(50)

    if turtle.ycor() > 250:
        break







screen.exitonclick()
