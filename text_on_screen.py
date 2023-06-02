from turtle import Turtle


def game_over():
    game_over = Turtle()
    game_over.color("white")
    game_over.hideturtle()
    game_over.write("Game over !!", move=False,
                    align="center", font=("Arial", 30, "bold"))


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 350)
        self.color("white")
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f'Score:{self.point}', move=False,
                   align="center", font=("Arial", 20, "bold"))

    def increase_score(self):
        self.point += 1
        self.update_score_board()

class Stage(Turtle):
    def __init__(self):
        super().__init__()
        self.stage = 1
        self.hideturtle()
        self.penup()
        self.goto(200, 350)
        self.color("white")
        self.show_stage()

    def show_stage(self):
        self.clear()
        self.write(f'Stage:{self.stage} ', move=False,
                   align="center", font=("Arial", 20, "bold"))

    def increase_stage(self):
        self.stage += 1
        self.show_stage()