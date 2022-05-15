from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 80, 'normal')
POSITION = (0, 200)
COLOR = 'white'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score_p1 = 0
        self.score_p2 = 0
        self.goto(POSITION)
        self.color(COLOR)
        self.update_scoreboard()
        self.speed('fastest')

    def update_scoreboard(self):
        self.write(f"{self.score_p1} : {self.score_p2} ", False, align=ALIGNMENT, font=FONT)

    def update_score_p1(self):
        self.score_p1 += 1
        self.clear()
        self.update_scoreboard()

    def update_score_p2(self):
        self.score_p2 += 1
        self.clear()
        self.update_scoreboard()

    def check_for_winner(self):
        if self.score_p1 == 10:
            self.clear()
            self.goto(0, 0)
            self.write("Player 1 wins!", False, align=ALIGNMENT, font=FONT)
            return True
        elif self.score_p2 == 10:
            self.clear()
            self.goto(0, 0)
            self.write("Player 2 wins!", False, align=ALIGNMENT, font=FONT)
            return True

