from turtle import Turtle
import time

BAR_MOVE_DISTANCE = 40
BAR_WIDTH = 4


class P_bar(Turtle):
    def __init__(self, x, y, color):
        super().__init__()  # inherit Turtle Class
        self.shape("square")
        self.fillcolor(color)
        self.shapesize(stretch_wid=1, stretch_len=BAR_WIDTH) #Standard turtle size is 20 pixcel x 20 pixcel
        self.setpos(x, y)

    def move_left(self):
        new_x = self.xcor() - BAR_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + BAR_MOVE_DISTANCE
        self.goto(new_x, self.ycor())


