from turtle import Turtle
import random
colors = ["red", "green", "blue", "yellow", "purple", "orange", "black"]
STARTING_MOVE_INCREMENT = 10
MOVE_INCREMENT = 5

class Car(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_INCREMENT

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-140,170)
            new_car.goto(x=370, y=random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for each_car in self.all_cars:
            each_car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

