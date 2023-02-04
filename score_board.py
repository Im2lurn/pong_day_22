from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(-80,200)
        self.write(self.l_score , font= ("courier",50,"normal"))
        self.goto(-15, 200)
        self.write(":", font=("courier", 50,"normal"))
        self.goto(50,200)
        self.write(self.r_score , font= ("courier",50,"normal"))

    def update_score(self):
        self.clear()
        self.goto(-15, 200)
        self.write(":", font=("courier", 50, "normal"))
        self.goto(-80, 200)
        self.write(self.l_score, font=("courier", 50,"normal"))
        self.goto(50, 200)
        self.write(self.r_score, font=("courier", 50,"normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

