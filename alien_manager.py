from turtle import Turtle

STARTING_POSITIONS = [[(-150, 250), (0, 250), (150, 250)],
                      [(-150, 200), (0, 200), (150, 200)],
                      [(-150, 150), (0, 150), (150, 150)]]
MOVE_DISTANCE = 2


class AlienManager:

    def __init__(self):
        self.aliens = []
        self.create_aliens()
        self.num_moves = 0

    def create_aliens(self):
        for row in STARTING_POSITIONS:
            for position in row:
                alien = Turtle()
                alien.penup()
                alien.shape("circle")
                alien.color("blue")
                alien.goto(position)
                self.aliens.append(alien)

    def delete_alien(self, alien):
        alien.clear()
        alien.hideturtle()
        self.aliens.remove(alien)

    def move_aliens(self):
        if self.num_moves < 15:
            for alien in self.aliens:
                alien.goto(alien.xcor() - MOVE_DISTANCE, alien.ycor())
            self.num_moves += 1
        elif self.num_moves < 30:
            for alien in self.aliens:
                alien.goto(alien.xcor() + MOVE_DISTANCE, alien.ycor())
            self.num_moves += 1
        elif self.num_moves < 45:
            for alien in self.aliens:
                alien.goto(alien.xcor() + MOVE_DISTANCE, alien.ycor())
            self.num_moves += 1
        elif self.num_moves < 60:
            for alien in self.aliens:
                alien.goto(alien.xcor() - MOVE_DISTANCE, alien.ycor())
            self.num_moves += 1
        else:
            self.num_moves = 0

