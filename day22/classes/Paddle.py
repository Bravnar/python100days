
from turtle import Turtle

SIZE = 20

class Paddle(Turtle):

    def __init__(self, position: tuple):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.score = 0

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def collision(self, ballPos: tuple) -> float:

        upper_bound = self.ycor() + SIZE
        lower_bound = self.ycor() - SIZE
        x_valid = False
        y_valid = False

        if ballPos[0] >= 330 or ballPos[0] <= -330:
            x_valid = True
        if ballPos[1] <= upper_bound and ballPos[1] >= lower_bound:
            y_valid = True

        if x_valid and y_valid: return True
        else: return False