from turtle import Turtle

FONT = ("Courier", 14, "bold")

class Tracker(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.count = 0;
        self.update_tracker()

    def update_tracker(self):
        self.clear()
        self.goto(-120, 210)
        self.write(f"States:{self.count} / 50", align="center", font=FONT)

    def incrCount(self):
        self.count += 1
        self.update_tracker()

