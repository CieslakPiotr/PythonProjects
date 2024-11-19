from turtle import Turtle
import random

colors = ["red", "blue", "green", "yellow", "grey", "brown", "pink"]
starting_coordinates = [(320, 0), (320, 60), (320, 120), (320, 180), (320, -60), (320, -120), (320, -180)]


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = 6

    def spawn_a_car(self):
        random_n = random.randint(0, 6)
        self.create_cars(starting_coordinates[random_n])

    def create_cars(self, position):
        car = Turtle()
        random_n = random.randint(0, 6)
        color = colors[random_n]
        car.shape("square")
        car.color(color)
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(position)
        self.cars.append(car)

    def car_moves(self):
        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())
