from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed('slowest')
        self.setheading(37)
        self.y_move = 10
        self.x_move = 10
        self.ball_speed = 0.1

    def bounce_y(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.7

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.bounce_y()

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def ball_speed_reset(self):
        self.ball_speed = 0.1
