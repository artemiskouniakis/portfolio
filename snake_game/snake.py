from turtle import Turtle


class Snake:
    def __init__(self, distance):
        self.snake = []
        self.distance = distance
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        x_axis = 0
        for segment in range(0,3):
            body = Turtle(shape="square")
            body.penup()
            body.color("white")
            body.goto(x = x_axis, y = 0)
            x_axis = x_axis - 20
            self.snake.append(body)

    def move(self):
        for item in range(len(self.snake)-1, 0, -1): #(start= len(snake)-1, stop=0, step=1
            new_x = self.snake[item - 1].xcor()
            new_y = self.snake[item - 1].ycor()
            self.snake[item].goto(x=new_x, y = new_y)
        self.snake[0].forward(self.distance)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_length(self):
        body = Turtle(shape="square")
        body.penup()
        body.color("white")
        body.goto(x = self.snake[-1].xcor(), y = self.snake[-1].ycor())
        self.snake.append(body)

