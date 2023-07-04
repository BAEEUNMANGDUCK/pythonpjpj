import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def move_counter_clock():
    turtle.left(10)


def move_clock():
    turtle.right(10)


def clear_drawing():
    turtle.reset()


screen.listen()

screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_counter_clock)
screen.onkey(key='d', fun=move_clock)
screen.onkey(key='c', fun=clear_drawing)
screen.exitonclick()
