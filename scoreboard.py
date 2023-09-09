from turtle import Turtle

FONT = ("Arial", 18, 'normal')
POSITION = (-240, -280)
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(POSITION)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self, game_result):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER.\n {game_result}", align=ALIGNMENT, font=FONT)
