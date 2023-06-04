from turtle import Turtle
import time


BALL_MOVE_DISTANCE = 3


class Ball(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.fillcolor(color)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(x, y)
        self.status = "game_on"

    def ball_move(self, p_bar, all_blocks, ball, score, stage,ball_speed):
        x_dir = BALL_MOVE_DISTANCE+ball_speed
        y_dir = BALL_MOVE_DISTANCE+ball_speed
        ball_is_on = True
        self.status = "game_on"

        while ball_is_on:
            self.goto(self.xcor() + x_dir, self.ycor() + y_dir)


            if 305 > self.xcor() > 290:
                x_dir = x_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if -305 < self.xcor() < -290:
                x_dir = x_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if 405 > self.ycor() > 390:
                y_dir = y_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            if self.ycor() < -390:  # if ball go out of bottom screen
                self.status = "game_off"
                ball_is_on = False  # move out roop




            if p_bar.xcor() - 40 < self.xcor() < p_bar.xcor() + 40 and self.ycor() == p_bar.ycor() + 10:
                # if p_bar.distance(ball) < 20:
                y_dir = y_dir * -1
                self.goto(self.xcor() + x_dir, self.ycor() + y_dir)

            # check if ball hits blocks. If yes, bound ball and erase block
            for block in all_blocks:
                if block.distance(ball) < 25:
                    all_blocks.remove(block)
                    # print(all_blocks)
                    score.increase_score()

                    block.fillcolor("black")
                    y_dir = y_dir * -1
                    self.goto(self.xcor() + x_dir, self.ycor() + y_dir)


            if not all_blocks:
                ball_is_on = False
                stage.increase_stage()

                # return "up_stage"

            # return score