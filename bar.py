from turtle import Turtle


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

    def ball_move(self):
        count = 0
        while count < 200:
            self.goto(self.xcor()+1, self.ycor()+1)
            count = count +1

#TODO move ball with some sleep


