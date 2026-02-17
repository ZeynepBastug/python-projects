from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()


    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
        self.goto(100, 220)
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1