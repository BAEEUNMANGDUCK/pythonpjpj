import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager= CarManager()
scoreboard = Scoreboard()
cre_car = 1 
screen.listen()

screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # 반복문이 6번 반복될 때 마다 한번씩 차 객체를 만듬 
    if cre_car % 6 == 0 :  
        car_manager.create_car()
    cre_car += 1
    car_manager.move()
    
    # 끝까지 도달했을 경우 
    if player.ycor() >= player.beat:
        player.beat_stage()
        scoreboard.upstage()
        car_manager.incre_carspeed()
    
    # 충돌 감지 
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            scoreboard.game_over()
            game_is_on = False
            break





screen.exitonclick()
