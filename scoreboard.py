from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        record = open("record.txt", mode="r")
        self.high_score = int(record.read())
        record.close()
        self.color("white")
        self.write(f"Score: {self.score}   Record: {self.high_score}", align="center", font=('Block', 15, 'normal'))

    def count_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}   Record: {self.high_score}", align="center", font=('Block', 15, 'normal'))

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            record = open("record.txt", mode="w")
            record.write(f"{self.high_score}")
            record.close()

        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=('Block', 15, 'normal'))
