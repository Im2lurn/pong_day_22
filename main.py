from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("MY_PONG_GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # to detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() == 340:
        ball.setx(320)
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.setx(-330)
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()

        score.l_point()

    if ball.xcor() < -390:
        ball.reset_position()

        score.r_point()

screen.exitonclick()
