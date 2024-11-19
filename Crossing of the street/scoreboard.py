from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-250, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level}", move=False, align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", move=False, align="center", font=("Arial", 16, "normal"))

    def next_level(self):
        self.level += 1
        self.update_scoreboard()
