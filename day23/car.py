from turtle import Turtle
from random import choice
from player import Player


START_X = 340
RAND_POS = tuple(range(-225, 276, 25))

class Car(Turtle):
    def __init__(self, color, move_speed):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(START_X, choice(RAND_POS))
        self.move_speed = move_speed

    def move(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())

    def collide(self, player: Player):
        if self.distance(player) < 30:
            player.die()

    def _reset_position(self):
        self.goto(START_X, choice(RAND_POS))
