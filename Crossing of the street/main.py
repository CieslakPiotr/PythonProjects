from turtle import Screen
from animal import Animal
from cars import Cars
from scoreboard import Scoreboard
import time

screen = Screen()
animal = Animal()
car = Cars()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Road crossing")
screen.tracer(0)

game_is_on = True

screen.listen()
screen.onkey(animal.up, "Up")
screen.onkey(animal.right, "Right")
screen.onkey(animal.left, "Left")

while game_is_on:
    screen.update()
    car.spawn_a_car()
    car.car_moves()
    time.sleep(0.1)

    for vehicle in car.cars:
        if animal.distance(vehicle) < 20:
            game_is_on = False
            score.game_over()

    if animal.ycor() > 200:
        car.speed += 1
        animal.next_level()
        score.next_level()

screen.exitonclick()
