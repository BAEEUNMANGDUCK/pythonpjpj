from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def plus_score(self):
        self.score += 1
        self.clear()
        self.create_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg="Game Over", align="center", font=FONT)
