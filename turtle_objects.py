import time
from turtle import *

class Paddle(Turtle):
    def __init__(self, move_s=30):
        super().__init__()
        self.penup()
        self.setheading(0)
        self.shape("square")
        self.shapesize(stretch_len=7, stretch_wid=1.0)

        self.teleport(x=0, y=-340)
        self.move_s = move_s

    def move_right(self):
        if self.xcor() < 270:
            self.goto(self.xcor() + self.move_s, self.ycor())

    def move_left(self):
        if self.xcor() > -270:
            self.goto(self.xcor() - self.move_s, self.ycor())

class Ball(Turtle):
    def __init__(self, move_x, move_y):
        super().__init__()
        self.penup()
        self.teleport(x=0, y=-300)
        self.setheading(0)
        self.shape("circle")

        self.move_x = move_x
        self.move_y = move_y

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y

        self.goto(new_x, new_y)

    def reset(self):
        self.teleport(0, 0)
        time.sleep(3)

    def bounce_x(self):
        self.move_x *= -1

    def bounce_y(self):
        self.move_y *= -1

class Block(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.setheading(0)
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.penup()

        self.teleport(x=x, y=y)


    def destroy(self):
        self.hideturtle()
        self.teleport(x=-500, y=-500)

class BallBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-350, 320)

        self.font = ("Arial", 25, "normal")
        self.balls = 4

        self.write(self.balls, font=self.font)

    def remove_life(self):
        self.balls -=1
        self.clear()
        self.write(self.balls, font=self.font)

        if self.balls == 0:
            self.clear()
            self.goto(-350, 0)
            self.write("GAME OVER", font=self.font)
