from turtle import Turtle

STARTING_POSITIONS = [(-200, -200), (-75, -200), (75, -200), (200, -200)]


class BarrierManager:

    def __init__(self):
        self.barriers = []
        self.create_barriers()

    def create_barriers(self):
        for position in STARTING_POSITIONS:
            barrier = Turtle()
            barrier.penup()
            barrier.color("yellow")
            barrier.shape("square")
            barrier.shapesize(stretch_wid=1, stretch_len=2)
            barrier.goto(position)
            self.barriers.append(barrier)

    def delete_barrier(self, barrier):
        barrier.clear()
        barrier.hideturtle()
        self.barriers.remove(barrier)
