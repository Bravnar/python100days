from car import Car
from random import choice
from player import Player
from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_SPEED = 2


class CarManager:

    def __init__(self):
        self.level = 0
        self.cars: list[Car] = []
    
    def spawn_car(self):
        car = Car(choice(COLORS), MOVE_SPEED + (MOVE_SPEED * self.level))
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars[:]:
            car.move()
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)

    def monitor_collisions(self, player: Player, scoreboard: Scoreboard):
        for car in self.cars[:]:
            car.collide(player, scoreboard)

    def monitor_progress(self, player: Player, scoreboard: Scoreboard):
        if player.ycor() > 280:
            player.reset_position()
            self.wipe_cars()
            self.level += 1
            scoreboard.incrLevel()

    def wipe_cars(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()

    def getLevel(self):
        return self.level
            

