from turtle import Turtle
import time

BALL_MOVE_DISTANCE = 2

class Ball(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.fillcolor(color)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(x, y)


    def ball_move(self,p_bar):
        x_dir = BALL_MOVE_DISTANCE
        y_dir = BALL_MOVE_DISTANCE
        ball_is_on = True

        while ball_is_on:
            self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.xcor() == 290:
                x_dir = x_dir*-1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.xcor() == -290:
                x_dir = x_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.ycor() == 390:
                y_dir = y_dir *-1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.ycor() == -390:
                    ball_is_on = False

            print(f'ball{self.xcor(), self.ycor()}')
            print(f'bar{p_bar.xcor(), p_bar.ycor()}')

            # judget if ball hit bar
            if p_bar.xcor() -30 < self.xcor() < p_bar.xcor() +30 and self.ycor() == p_bar.ycor()+10:
                y_dir = y_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)



# TODO Pen up of ball
