from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'italic')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.color('white')
        self.speed(0)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'Score:  {self.score} High Score:   {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def tally_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def reset_high(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as data:
                data.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', move=False, align=ALIGNMENT, font=FONT)
