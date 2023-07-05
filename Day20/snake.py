from turtle import Turtle

# 변하지 않아야 할 상수들을 설정하는 것
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # snake 객체를 만들자마자 선언되거나 호출되는 변수또는 함수들을 넣음
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape='square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            # self.segments[0].setheading(90)
            # snake의 머리 부분을 쓸 일 이 많으니까 클래스에 전역으로 선언해둔다.
            self.head.setheading(UP)

    def down(self):
        # 조건문을 설정하는 이유 snake 게임에서 머리가 위, 아래, 오른쪽, 왼쪽을 향할 때 바로 아래, 위, 왼쪽, 오른쪽으로 움직일 수 없음
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
