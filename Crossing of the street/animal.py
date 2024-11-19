from turtle import Turtle


class Animal(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -260)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def right(self, **kwargs):
        new_x = self.xcor() + 15
        self.goto(new_x, self.ycor())

    def left(self, **kwargs):
        new_x = self.xcor() - 15
        self.goto(new_x, self.ycor())

    def next_level(self):
        self.goto(0, -260)
