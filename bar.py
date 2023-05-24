from turtle import Turtle, Screen, onkeypress


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

    Screen().onkeypress(move_left, "Left")
    Screen().onkeypress(move_right, "Right")
