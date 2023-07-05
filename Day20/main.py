import turtle as t
from snake import Snake
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
# screen.tracer(0):  코드들이 실행하는 과정을 스크린창에 출력하지 않음
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    # screen.update() 그동안 실행되었던 코드들이 스크린창에 업데이트 됨.
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()
