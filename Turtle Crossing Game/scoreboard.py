from turtle import Turtle

FONT = ('Courier', 24, 'normal')
TOP = (-110, 160)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_level = 0
        self.hideturtle()
        self.penup()
        self.goto(TOP)
        self.write(arg=f'Level:{self.starting_level}', align='center', font=FONT)

    def update_score(self):
        self.clear()
        self.write(arg=f'Level:{self.starting_level}', align='center', font=FONT)

    def increase_score(self):
        self.starting_level +=1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg='GAME OVER', align='center', font=FONT)



