
from turtle import Screen
from classes.Paddle import Paddle
from classes.Ball import Ball
from classes.Scoreboard import Scoreboard

import time

Y_BOUND = 280

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600, 2000, 100)
screen.title("Pong")
screen.tracer(0)
# screen.delay(10)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


def gameplay_loop():
    screen.update()
    ball.move()
    print(f"X: {r_paddle.xcor()}\nY: {r_paddle.ycor()}")
    # Detect collision with wall
    if ball.ycor() > Y_BOUND or ball.ycor() < -Y_BOUND:
        ball.bounce_wall()

    # Detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle(r_paddle)
    
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle(l_paddle)

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position(r_paddle)
        scoreboard.l_point()

    # Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position(l_paddle)
        scoreboard.r_point()

    screen.ontimer(gameplay_loop, 32)

game_is_on = True
gameplay_loop()

screen.exitonclick()