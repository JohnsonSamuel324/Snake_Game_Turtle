from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(x=0,y=270)
        self.display_score()

    def add_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 16, "bold"))

    def display_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 16, "bold"))