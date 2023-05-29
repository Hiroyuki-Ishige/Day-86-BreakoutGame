import time
from turtle import Screen
from bar import P_bar
from ball import Ball
from block import Block_Manager

# Fixed variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

# making screen object
sc = Screen()
sc.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
sc.bgcolor("black")
sc.title("Breakout")

# create initial screen --------------------------------
sc.tracer(0) #Turn off screen update. 0 is off, 1 is on

# Create player bar
p_bar = P_bar(x=0, y=-350, color="white")

# Create ball
ball = Ball(x=0, y=-340, color="white", )

# Create block
block_manager = Block_Manager()
block_manager.create_block()


# Set key listen ----------------------------------------
sc.listen()
sc.onkey(p_bar.move_left, "Left")
sc.onkey(p_bar.move_right, "Right")

# -------------------------------------------------------
sc.tracer(1) #Turn on screen update
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    # sc.update()

    # Ball starts moving after all initial screen created
    ball.ball_move(p_bar=p_bar)

    #TODO Check ball hit block
    # name.ball_hit_block(ball=ball)







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
# TODO Set up block
# TODO Set up name, Score
# TODO Set up judge hitting with block and erase block once it's hit with ball

# TODO Set up score recording system
