from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


scoreboard = Scoreboard()


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    if ball.xcor() > 330 and ball.distance(right_paddle) < 50:
        ball.bounce_x()
    elif ball.xcor() < -330 and ball.distance(left_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 380:
        scoreboard.update_score_p1()
        ball.reset_position()
        ball.ball_speed_reset()
    elif ball.xcor() < -380:
        scoreboard.update_score_p2()
        ball.reset_position()
        ball.ball_speed_reset()
    if scoreboard.check_for_winner():
        game_is_on = False
    time.sleep(ball.ball_speed)

screen.exitonclick()
