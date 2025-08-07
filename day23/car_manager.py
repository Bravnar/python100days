from car import Car
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 2


class CarManager:

    def __init__(self):
        self.cars: list[Car] = []
    
    def spawn_car(self):
        car = Car(choice(COLORS), MOVE_INCREMENT)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars[:]:
            car.move()
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    def monitor_collisions(self, player):
        for car in self.cars[:]:
            car.collide(player)

