from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.create_scoreboard()
        
    
    def create_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.write(arg=f"Level:{self.level}", align="left", font=FONT)
    
    
    def upstage(self):
        self.clear()
        self.level += 1
        self.create_scoreboard()
    
    
    def game_over(self):
        self.clear()
        self.hideturtle()
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align="center", font=FONT)