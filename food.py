from turtle import Turtle
import random

#screen_size
# WIDTH = 600
# HEIGHT = 600

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        #self.speed("faster")


    def make_new_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)  # Give every time a new random position(x,y) to the food.


