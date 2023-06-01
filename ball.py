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

    def ball_move(self, p_bar, all_blocks, ball, score):
        x_dir = BALL_MOVE_DISTANCE
        y_dir = BALL_MOVE_DISTANCE
        ball_is_on = True
        score_count = 0

        while ball_is_on:
            self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.xcor() == 290:
                x_dir = x_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.xcor() == -290:
                x_dir = x_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.ycor() == 390:
                y_dir = y_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.ycor() == -390:
                ball_is_on = False  # move out roop

            if p_bar.xcor() - 40 < self.xcor() < p_bar.xcor() + 40 and self.ycor() == p_bar.ycor() + 10:
                # if p_bar.distance(ball) < 20:
                y_dir = y_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            # check ball hits block. If ball hit, bound ball and erase block
            point = 0
            for block in all_blocks:
                if block.distance(ball) < 20:
                    all_blocks.remove(block)
                    # print(all_blocks)
                    score.increase_score()

                    block.fillcolor("black")
                    y_dir = y_dir * -1
                    self.goto(self.xcor() + x_dir, self.ycor() + y_dir)
