from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 3
FINISH_LINE_Y = 280
FULL_HP = 3


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

        self.health = FULL_HP
        

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_backward(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def collide(self, collider):
        if self.distance(collider) < 40:
            self._die()

    def die(self):
        self.health -= 1
        print(f"Player health: {self.health}")
        self.reset_position()

    def reset_position(self):
        self.goto(STARTING_POSITION)
