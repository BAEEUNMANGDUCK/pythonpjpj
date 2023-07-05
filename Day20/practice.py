from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.listen()


def up():
    t.setheading(90)


def down():
    t.setheading(270)


def left():
    t.setheading(180)


def right():
    t.setheading(0)


screen.onkey(fun=up, key='Up')
screen.onkey(fun=down, key='Down')
screen.onkey(fun=left, key='Left')
screen.onkey(fun=right, key='Right')

game_is_on = True
while game_is_on:
    t.forward(20)

screen.exitonclick()
