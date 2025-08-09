from turtle import Turtle

FONT = ("Courier", 12, "normal")

class State(Turtle):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.color("black")
        self.penup()
        self.hideturtle()

    def slide_state(self, coords):
        self.clear()
        self.goto(coords)
        self.write(f"{self.name}", align="center", font=FONT)

