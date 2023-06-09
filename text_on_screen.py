from turtle import Turtle
import pprint

def game_over(score_list):
    game_over = Turtle()
    game_over.color("white")
    game_over.hideturtle()
    game_over.penup()
    game_over.goto(0,150)

    game_over.write(f'Game over !!\n\n'
                    'Top 5 High score\n'
                    f'Player:{score_list[0]["player"]}'
                    ,


                    move=False,
                    align="center", font=("Arial", 25, "bold"))


class Score(Turtle): # show score on screen
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

class Stage(Turtle): # show stage number on screen
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

class PlayerName(Turtle): #show player name on screen
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, -380)
        self.color("white")



    def show_name(self, player):
        self.clear()
        self.write(f'Player:{player} ', move=False,
                   align="left", font=("Arial", 20, "bold"))
