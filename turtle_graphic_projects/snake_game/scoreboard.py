from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 14, 'normal')
TEXT_COLOR = "white"
SCORE_FOR_FOOD = 1

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("game_data.txt", mode= "r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color(TEXT_COLOR)
        self.teleport(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}" ,align =ALIGNMENT, font=FONT )

    def increase_score(self):
        self.score += SCORE_FOR_FOOD
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("game_data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

