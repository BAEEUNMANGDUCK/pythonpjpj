import turtle
import turtle as t
import random
# 각 객체는 서로 다른 속성과 메서드를 사용할 수 있음

is_race_on = True
screen = t.Screen()
# 다른 사람이 보기에도 쉽게 keywords argument를 하는 것이 좋음.
screen.setup(width=500, height=400)

# 경주에 승리할 거북이 객체 예상
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:")

# 거북이 색깔과 좌표를 인덱스로 설정하기 위해 정의해놓은 리스트
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_y = [-100, -60, -20, 20, 60, 100]
# turtle 객체를 담기 위한 리스트
all_turtles = []

# 6개의 객체 만들기
for i in range(6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=turtle_y[i])
    all_turtles.append(new_turtle)

# print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        # turtle의 크기가 40인데 250지점에 도달할 때 탐지하면 이미 결승전을 지나있어서 230으로 해야 화면 끝에 닿자마자 승리한 거북이를 나타낼 수 있음.
        if turtle.xcor() > 230:
            if user_bet == turtle.color()[0]:
                print(f"{turtle.color()[0]} is a Winner. You win!")
            else:
                print(f"{turtle.color()[0]} is a winner. You lose!")
            is_race_on = False


screen.exitonclick()
