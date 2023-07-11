from turtle import Turtle
import random 
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self):
        # 차 객체를 담을 리스트 
        self.all_cars = []
        self.car_speed = 5
        
    
    
    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape('square')
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid= 1, stretch_len=2)
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)
        
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def incre_carspeed(self):
        self.car_speed += MOVE_INCREMENT