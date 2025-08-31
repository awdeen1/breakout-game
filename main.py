import time
from turtle_objects import *
from turtle import *

screen = Screen()

ball = Ball(move_x=10, move_y=-10)
paddle = Paddle(move_s=35)
ball_board = BallBoard()

blocks = []
for row in range(150, 350, 50):
     for column in range(-300, 350, 50):
         blocks.append(Block(x=column, y=row))


screen.onkey(paddle.move_left, "a")
screen.onkey(paddle.move_right, "d")
screen.listen()

while ball_board.balls > 0:
    time.sleep(0.02)
    ball.move()

    if ball.xcor() > 330 or ball.xcor() < -330:
        ball.bounce_x()

    if ball.ycor() > 350:
        ball.bounce_y()
    elif ball.ycor() < -350:
        ball_board.remove_life()
        ball.reset()

    if ball.distance(paddle) < 60 and ball.move_y != 10:
        ball.bounce_y()

    for block in blocks:
        if block.distance(ball) < 40:
            block.destroy()
            blocks.remove(block)
            ball.bounce_y()



screen.mainloop()