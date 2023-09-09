from turtle import Screen
from ship import Ship
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

player = Ship()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
