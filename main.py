from turtle import Screen
from ship import Ship
from projectile_manager import ProjectileManager
from barrier_manager import BarrierManager
from alien_manager import AlienManager
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

# initialize all the needed objects
game_speed = 0.1
player = Ship()
scoreboard = Scoreboard()
b_manager = BarrierManager()
a_manager = AlienManager()
player_p_manager = ProjectileManager(player, "player")
# choose random alien ship to shoot projectile
alien_p_manager = ProjectileManager(random.choice(a_manager.aliens), "alien")

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(player_p_manager.create_projectile, "space")

is_game_on = True
while is_game_on:
    time.sleep(game_speed)
    screen.update()

    # end game if there are no more aliens
    if not a_manager.aliens:
        is_game_on = False

    # move aliens back and forth
    a_manager.move_aliens()

    '''moves player-created projectile across the screen once the user has
    fired using the space bar'''
    if player_p_manager.projectile:
        player_p_manager.move_projectile()

        # detect player's projectile collision with barrier
        for barrier in b_manager.barriers:
            if player_p_manager.projectile and player_p_manager.projectile.distance(barrier) < 20:
                b_manager.delete_barrier(barrier)
                player_p_manager.delete_projectile()

        # detect player's projectile collision with aliens
        for alien in a_manager.aliens:
            if player_p_manager.projectile and player_p_manager.projectile.distance(alien) < 20:
                a_manager.delete_alien(alien)
                player_p_manager.delete_projectile()
                scoreboard.increase_score()
                game_speed = game_speed * 0.9

    # fire projectile from random alien
    if not alien_p_manager.projectile:
        alien_p_manager = ProjectileManager(random.choice(a_manager.aliens), "alien")
        alien_p_manager.create_projectile()
    alien_p_manager.move_projectile()

    # detect alien projectile collision with barrier
    for barrier in b_manager.barriers:
        if alien_p_manager.projectile and alien_p_manager.projectile.distance(barrier) < 20:
            b_manager.delete_barrier(barrier)
            alien_p_manager.delete_projectile()

    # detect alien projectile collision with player ship and end game
    if alien_p_manager.projectile and alien_p_manager.projectile.distance(player) < 20:
        player.destroy_ship()
        alien_p_manager.delete_projectile()
        screen.update()
        is_game_on = False

if a_manager.aliens:
    scoreboard.game_over("Better luck next time.")
else:
    scoreboard.game_over("Winner!")

screen.exitonclick()
