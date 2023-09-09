from turtle import Turtle

STARTING_POSITION = (0, -260)
MOVING_DISTANCE = 10


class Ship(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("triangle")
        self.color("green")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def destroy_ship(self):
        self.clear()
        self.hideturtle()

    def move_right(self):
        self.goto(self.xcor() + MOVING_DISTANCE, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - MOVING_DISTANCE, self.ycor())
