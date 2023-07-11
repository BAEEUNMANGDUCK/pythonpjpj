from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.xmove = 10
        self.ymove = 10 
        self.move_speed = 0.1
    
    
    
    
    def move(self):
        cur_x = self.xcor()+ self.xmove
        cur_y = self.ycor() + self.ymove
        self.goto(cur_x , cur_y )
    
    def bounce_y(self):
        self.ymove *= -1
    
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9
    
    def reset_move(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.xmove *= -1