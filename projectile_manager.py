from turtle import Turtle

MOVE_DISTANCE = 10


class ProjectileManager:
    def __init__(self, ship, source):
        self.projectile = None
        self.ship = ship
        self.source = source

    def create_projectile(self):
        if not self.projectile:
            self.projectile = Turtle()
            self.projectile.shape("square")
            self.projectile.penup()
            self.projectile.shapesize(stretch_len=0.5, stretch_wid=0.1)

            if self.source == "player":
                self.projectile.color("white")
                self.projectile.setheading(90)
                self.projectile.goto(self.ship.xcor(), self.ship.ycor() + 20)
            elif self.source == "alien":
                self.projectile.color("purple")
                self.projectile.setheading(270)
                self.projectile.goto(self.ship.xcor(), self.ship.ycor() - 20)

    def move_projectile(self):
        self.projectile.forward(MOVE_DISTANCE)
        if self.source == "player":
            if self.projectile.ycor() > 300:
                self.delete_projectile()
        elif self.source == "alien":
            if self.projectile.ycor() < -300:
                self.delete_projectile()

    def delete_projectile(self):
        self.projectile.clear()
        self.projectile.hideturtle()
        self.projectile = None
