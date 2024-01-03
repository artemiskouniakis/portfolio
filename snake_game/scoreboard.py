from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.color("white")
        self.goto(x=0,y=260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg = f"Score: {self.current_score}", align="center", font=("Arial", 24, "normal"))


    def increase(self):
        self.current_score += 10
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(x=0,y=0)
        self.color("orange")
        self.write(arg = f"Game Over! Your Score is: {self.current_score}", align="center", font=("Arial", 24, "normal"))