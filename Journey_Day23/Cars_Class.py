import random
from turtle import Turtle,Screen

colors_list = [
    "red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white",
    "cyan", "magenta", "lime", "maroon", "navy", "olive", "teal", "turquoise", "coral", "gold",
    "chocolate", "darkgreen", "darkblue", "deepskyblue", "hotpink", "indigo", "lavender",
    "lightblue", "lightgreen", "salmon", "sienna", "skyblue", "tan", "tomato", "violet", "wheat"
]

MOVE_DISTANCE=10
INCREMENT=20

class Cars():
    def __init__(self):
        self.Car_segment = []
        self.car_speed=MOVE_DISTANCE

    def create_car(self):
        random_number=random.randint(1,6)
        if random_number==5:

            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(colors_list))
            new_car.shapesize(stretch_wid=1.25, stretch_len=3)
            self.random_y = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, self.random_y)
            self.Car_segment.append(new_car)

    def move_cars(self):
        for all_cars in self.Car_segment:
            all_cars.setheading(180)
            all_cars.forward(self.car_speed)

    def level_up(self):
        self.car_speed=self.car_speed+INCREMENT








