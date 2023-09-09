from turtle import Screen
from ship import Ship
from projectile_manager import ProjectileManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player = Ship()
manager = ProjectileManager(player)

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(manager.create_projectile, "space")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    '''moves player-created projectile across the screen once the user has
    fired using the space bar'''
    if manager.projectile:
        manager.move_projectile()

screen.exitonclick()
