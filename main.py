from turtle import Screen
from ship import Ship
from projectile_manager import ProjectileManager
from barrier_manager import BarrierManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player = Ship()
p_manager = ProjectileManager(player)
b_manager = BarrierManager()

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(p_manager.create_projectile, "space")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    '''moves player-created projectile across the screen once the user has
    fired using the space bar'''
    if p_manager.projectile:
        p_manager.move_projectile()

        # detect projectile collision with barrier
        for barrier in b_manager.barriers:
            if p_manager.projectile and p_manager.projectile.distance(barrier) < 20:
                b_manager.delete_barrier(barrier)
                p_manager.delete_projectile()

screen.exitonclick()
