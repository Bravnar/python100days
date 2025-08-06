
from turtle import Turtle
from classes.Paddle import Paddle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.dir_x = 5
        self.dir_y = 5
        self.last_bounce: Paddle = None

    def move(self):
        new_x = self.xcor() + self.dir_x
        new_y = self.ycor() + self.dir_y
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.dir_y *= -1

    def bounce_paddle(self, collider: Paddle):
        if (self.last_bounce == collider):
            return
        self.dir_x *= -1
        self.last_bounce = collider

    def reset_position(self, collider: Paddle):
        self.goto(0, 0)
        self.bounce_paddle(collider)