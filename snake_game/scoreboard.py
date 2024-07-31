from turtle import Turtle

CENTER = 'center'
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file='data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=170)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score {self.high_score}", move=False, align=CENTER, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file='data.txt', mode='w') as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move=False, align=CENTER, font=FONT)
    def increase_score(self):
        self.score += 1
        self.update_score()
