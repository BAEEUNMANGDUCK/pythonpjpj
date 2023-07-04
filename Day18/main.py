import turtle as t
# import heroes
import random

# print(heroes.gen())
turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


turtle.shape('turtle')
turtle.color('red')

# Draw a square
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

for _ in range(15):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)


for i in range(3, 11):
    turtle.color(random.choice(colors))
    for _ in range(i):
        turtle.forward(100)
        turtle.right(360 / i)



#
turtle.speed("fastest")
turtle.pensize(5)


# def turn_right():
#     turtle.right(90)
#
#
# def turn_left():
#     turtle.left(90)
#
#
# def turn_around():
#     turtle.right(180)
#
#
# randoms = {'left': turn_left, 'right': turn_right, 'around': turn_around}
# l_or_r = ['left', 'right', 'around']
ways = [0, 90, 180, 270]
while True:
    turtle.color(random_color())
    turtle.setheading(random.choice(ways))
    turtle.forward(20)

count = 0
x = 5
while count < 360/x:
    turtle.color(random_color())
    turtle.circle(100)
    turtle.left(x)
    count += 1


screen = t.Screen()
screen.exitonclick()
