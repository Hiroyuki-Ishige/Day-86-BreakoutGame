from turtle import Screen
from turtle import *

# making turtle object
sc = Screen()
sc.setup(width=600, height=800)
sc.bgcolor("black")
sc.title("Breakout")

#Create player bar
p_bar = Turtle("square")
p_bar.fillcolor("white")
p_bar.turtlesize(stretch_wid=2, stretch_len=5)
#TODO set first position of p_bar



# keep screen show
mainloop()

#TODO set up Class of
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
#TODO Set up ball and it's move
#TODO Set up bar and it's move
#TODO Set up name, Score
#TODO Set up block
#TODO Set up judge hitting with block and erase block once it's hit with ball

#TODO Set up score recording system


