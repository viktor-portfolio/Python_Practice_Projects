from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')
TEXT_COLOR = "white"
SCORE_FOR_FOOD = 1

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.teleport(0, 280)
        self.written_score()

    def written_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align =ALIGNMENT, font=FONT )

    def increase_score(self):
        self.score += SCORE_FOR_FOOD
        self.written_score()

    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
