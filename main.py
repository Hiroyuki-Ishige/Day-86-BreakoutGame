import time
from datetime import datetime
from turtle import Screen, Turtle
from bar import P_bar
from ball import Ball
from block import Block_Manager
from text_on_screen import game_over, Score, Stage, PlayerName

# Fixed variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# making screen object
sc = Screen()
sc.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
sc.bgcolor("black")
sc.title("Breakout")

# create initial screen --------------------------------
sc.tracer(0)  # Turn off screen update. 0 is off, 1 is on

# Create player bar
p_bar = P_bar(x=0, y=-330, color="white")

# Create ball
ball = Ball(x=0, y=-320, color="white", )

# Show score
score = Score()
stage = Stage()

# Show player name
player_name = sc.textinput("Welcome to Breakout game!!", "Input player name")
player = PlayerName()
player.show_name(player_name)

# Set key listen ----------------------------------------
sc.listen()
sc.onkey(p_bar.move_left, "Left")
sc.onkey(p_bar.move_right, "Right")

# -------------------------------------------------------


game_is_on = True
ball_speed = 0
while game_is_on:
    time.sleep(0.01)

    # Create block
    block_manager = Block_Manager()  # Create instance
    block_manager.create_block()  # Call method
    sc.tracer(1)  # Turn on screen update

    # Ball starts moving after all initial screen created
    ball.ball_move(p_bar=p_bar, all_blocks=block_manager.all_blocks, ball=ball,
                   score=score, stage=stage, ball_speed=ball_speed)
    if ball.status == "game_on":  # if ball roop is out by all block clear
        sc.tracer(0)
        ball.goto(0, -340)
        if ball_speed < 11:
            ball_speed += 1
        print(ball_speed)
    else:
        game_is_on = False

        score_dict = {
            "name":player_name,
            "score":str(getattr(score, "point")),
            "date&time": datetime.now().strftime("%d/%b/%Y %H:%M:%S")
        }

        with open("record_score.txt", "w") as f:
            f.write(str(score_dict))

game_over()



sc.exitonclick()
# mainloop()


"""
Player bar
Ball
1. move constantly
2. detect collision with wall and block
3. detect collision with player bar
4. detect when people misses

Block
1. Layout block
1. erase block when it's hit with ball

Score
1. Add score when ball hit's block

"""
# TODO Set up score recording system.Write to file for multiple score (now only 1 score)
