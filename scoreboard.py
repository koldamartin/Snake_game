from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.score_num = 0
        # search data1.txt for high score number
        with open("data1.txt") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score_num} High score: {self.high_score}", move=False, align=ALIGMENT, font=FONT)

    def score_point(self):
        self.score_num += 1
        self.update_scoreboard()

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("data1.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score_num = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER", move=False, align=ALIGMENT, font=FONT)



