from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
# screen.tracer(0):  코드들이 실행하는 과정을 스크린창에 출력하지 않음
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

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

    # Detect collision with food.  use distance() method
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.plus_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        score.game_over()
        game_is_on = False

    # Detect collision with tail.
    # if head collides with any segment in the tail:
    # trigger game_over.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False



screen.exitonclick()
