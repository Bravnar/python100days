from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
manager = CarManager()

def gameplay_loop():

    global game_is_on
    
    if not game_is_on:
        return

    screen.update()

    screen.listen()
    screen.onkeypress(player.move_forward, 'w')
    screen.onkeypress(player.move_backward, 's')

    manager.move_cars()
    manager.monitor_collisions(player)

    if player.health == 0:
        game_is_on = False

    screen.ontimer(gameplay_loop, 32)

def spawn_car_loop():
    manager.spawn_car()
    screen.ontimer(spawn_car_loop, 1000)

if __name__ == "__main__":

    if game_is_on:
        gameplay_loop()
        spawn_car_loop()

    if not game_is_on:
        print("GAME OVER!")
    

    screen.exitonclick()