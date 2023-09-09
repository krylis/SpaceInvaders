from turtle import Turtle

STARTING_POSITION = (0, -260)


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.color("green")
        self.setheading(90)
        self.goto(STARTING_POSITION)
