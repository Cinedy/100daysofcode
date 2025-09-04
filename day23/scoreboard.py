from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 1
        self.increase_level()

    def increase_level(self): #and update scoreboard
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", move=False, align="center", font=FONT)
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)

#level and gameover