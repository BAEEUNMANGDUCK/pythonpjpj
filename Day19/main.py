import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forwards():
    turtle.forward(10)


screen.listen()

# 함수 안에 함수를 인자로 전달 Higher Order function (고차 함수)
screen.onkey(fun=move_forwards, key='space')


screen.exitonclick()
