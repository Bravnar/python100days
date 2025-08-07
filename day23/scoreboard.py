from turtle import Turtle

FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.health = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 275)
        self.write(f"Level:{self.level}", align="center", font=FONT)
        self.goto(-125, 275)
        self.write(f"Health:{self.health}", align="center", font=FONT)

    def incrLevel(self):
        self.level += 1
        self.update_scoreboard()

    def decrHealth(self):
        self.health -= 1
        self.update_scoreboard()
