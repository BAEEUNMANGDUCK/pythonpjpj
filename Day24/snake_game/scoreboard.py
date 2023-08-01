from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt',mode='r') as f:
            score = f.read()
        self.high_score = int(score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open('data.txt',mode='w') as f:
            f.write(str(self.high_score))
        self.score = 0 
        self.update_scoreboard()
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()