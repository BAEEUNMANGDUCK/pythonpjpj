import pandas as pd
import turtle
screen = turtle.Screen()

# turtle 배경에 미국 지도 넣기 
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# 창에 제목 넣기 
screen.title('U.S. States Game')

# 맞춘 주 저장할 빈 리스트 
correct_list = []

# 판다스 라이브러리로 csv 파일 불러오기 
datas = pd.read_csv('50_states.csv')

# 주만 따로 리스트 형태로 만듬 

states_list = datas.state.to_list()

# 맞춘 점수 
score = 0 


while len(correct_list) < 50:
    if score == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    else:
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")

    if answer_state == 'exit':
        remained_states = []
        
        for state in states_list:
            if state in correct_list:
                continue
            else:
                remained_states.append(state)

        print(remained_states)
        new_data = pd.DataFrame(remained_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state.title() in states_list and answer_state not in correct_list:
        correct_list.append(answer_state.title())
        get_state = datas[datas.state == answer_state.title()]
        x = get_state.x.item()
        y = get_state.y.item()
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        name.goto(x=x, y=y)
        name.write(arg=f"{answer_state}", font=("Arial", 8, "normal"))
        score += 1
    else:
        continue


# states_to_learn.csv








