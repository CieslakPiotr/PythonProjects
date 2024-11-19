from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.Score} High Score: {self.high_score}", move=False, align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.Score > self.high_score:
            self.high_score = self.Score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.Score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.Score += 1
        self.update_scoreboard()