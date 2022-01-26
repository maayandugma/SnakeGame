from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()


    def update_score(self):
        self.write(f"score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear() #Delete the previous score from the screen
        self.write(f"score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME-OVER", align="center", font=("Arial", 20, "normal"))