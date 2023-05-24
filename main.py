from turtle import Screen
from turtle import *
from bar import P_bar

# making turtle object
sc = Screen()
sc.setup(width=600, height=800)
sc.bgcolor("black")
sc.title("Breakout")
sc.tracer(0) #Turn off screen update. 0 is off, 1 is on

# Create player bar
p_bar = P_bar(0, -350, color="white")
p_bar_2 = P_bar(100, -350, color="blue")
# p_bar = Turtle("square")
# p_bar.fillcolor("white")
# p_bar.shapesize(stretch_wid=1, stretch_len=4)
# p_bar.setpos(0, -350)

# Move player bar
# def move_left():
#     new_x = p_bar.xcor() - 20
#     p_bar.goto(new_x, p_bar.ycor())
#
# def move_right():
#     new_x = p_bar.xcor() + 20
#     p_bar.goto(new_x, p_bar.ycor())

def move_up():
    new_y = p_bar.ycor() + 20
    p_bar.goto(p_bar.xcor(), new_y)

def move_down():
    new_y = p_bar.ycor() - 20
    p_bar.goto(p_bar.xcor(), new_y)


sc.listen()
# sc.onkeypress(move_left, "Left")
# sc.onkeypress(move_right, "Right")
# sc.onkeypress(move_up, "Up")
# sc.onkeypress(move_down, "Down")

game_is_on = True
while game_is_on:
    sc.update()

# keep screen show
# sc.exitonclick()
mainloop()

# TODO set up Class of
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
# TODO Set up ball and it's move
# TODO Set up bar and it's move
# TODO Set up name, Score
# TODO Set up block
# TODO Set up judge hitting with block and erase block once it's hit with ball

# TODO Set up score recording system
