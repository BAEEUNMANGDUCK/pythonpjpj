from turtle import Turtle
FONT = ('Courier', 25, 'normal')

class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0   
        self.create_scoreboard()
    
    def create_scoreboard(self):
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=250)
        self.write(arg=f"{self.l_score} : {self.r_score}",align="center", font=FONT)
        
    def score_up(self,winner):
        self.clear()
        if winner == 'l':
            self.l_score += 1
        else:
            self.r_score += 1
        self.create_scoreboard()