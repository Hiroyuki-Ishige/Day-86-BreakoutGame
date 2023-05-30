from turtle import Turtle

def game_over():
    game_over = Turtle()
    game_over.color("white")
    game_over.hideturtle()
    game_over.write("Game over !!", move=False,
                    align="center", font=("Arial", 30, "bold"))

def score():
    score = Turtle()
    score.penup()
    score.color("white")
    score.hideturtle()
    score.setpos(0, 350)
    score.write("Score:", move=False,
                    align="center", font=("Arial", 20, "bold"))
