# create the screen 
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.title('Pong Game')
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

L_POSITION = (-350, 0)
R_POSITION = (350, 0)

l_paddle = Paddle(L_POSITION)
r_paddle = Paddle(R_POSITION)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=r_paddle.paddle_up, key="Up")
screen.onkey(fun=r_paddle.paddle_down, key="Down")

screen.onkey(fun=l_paddle.paddle_up, key="w")
screen.onkey(fun=l_paddle.paddle_down, key="s")

end_of_game = False


while not end_of_game:
    time.sleep(ball.move_speed)
    screen.update()
    
    # ball이 위아래 벽에 부딪혔을 시 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ball.move()
    
    # ball이 r_paddle, l_paddle에 부딪혔을 시 
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    # 패들을 지나쳤을 때, 굳이 2개로 나누는 이유? 점수 측정할 때 편해서
    
    if ball.xcor() > 380:
        ball.reset_move()
        scoreboard.score_up(winner='l')
    if ball.xcor() < -380:
        ball.reset_move()
        scoreboard.score_up(winner='r')

screen.exitonclick()

# make a scoreboard 
# make a ball
# make two paddles(sticks)

