import time
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.set_new_record = False
        self.get_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.display_score()

    def add_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Arial", 16, "bold"))
        self.goto(245, 280)
        self.write(f"High Score: {self.highscore}", move=False, align="center", font=("Arial", 10, "bold"))
        if self.set_new_record:
            self.new_record()

    def get_highscore(self):
        with open("data.txt", "r") as file:
            content = file.read()
            self.highscore = int(content)

    def set_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.set_new_record = True
        with open("data.txt", "w") as file:
            file.write(str(self.highscore))

    def new_record(self):
        self.goto(245, 265)
        # Write that user made new record
        self.color("yellow")
        self.write("New record!", move=False, align="center", font=("Arial", 8, "bold"))
        # Set back to white
        self.color("white")
        self.set_new_record = False

    def desc_to_start(self):
        self.goto(0,25)
        self.write(arg="Press space to start...", move=False, align="center", font=("Arial", 16, "bold"))

    def reset(self):
        self.set_highscore()
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 16, "bold"))