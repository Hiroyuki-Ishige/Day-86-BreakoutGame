from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Block_Manager:

    def __init__(self):
        self.all_blocks =[]
    def create_block(self):
        number_block = range(0, 8)
        rows = range (0,4)
        for row in rows:
            for i in number_block:
                new_block = Turtle("square")
                new_block.penup()
                new_block.color(random.choice(COLORS))
                new_block.shapesize(stretch_wid=1, stretch_len=3)
                new_block.setpos(x=-250 + 20 + i * 65, y=330-25*row)
                self.all_blocks.append(new_block)
                # print(self.all_blocks)

