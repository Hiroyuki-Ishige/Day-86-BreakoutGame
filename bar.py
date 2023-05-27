from turtle import Turtle
import time


class P_bar(Turtle):
    def __init__(self, x, y, color):
        super().__init__()  # inherit Turtle Class
        self.shape("square")
        self.fillcolor(color)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.setpos(x, y)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())


class Ball(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("circle")
        self.fillcolor(color)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(x, y)


    def ball_move(self,p_bar):
        x_dir = 1
        y_dir = 1
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

            if p_bar.xcor() -30 < self.xcor() < p_bar.xcor() +30 and self.ycor() == p_bar.ycor():
                y_dir = y_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)



# TODO Pen up of ball
