from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'italic')

class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.color('white')
        self.speed(0)
        self.display_score()

    def display_score(self):
        center = 'center'
        self.write(f'Score:  {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def tally_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONT)