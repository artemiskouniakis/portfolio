# import turtle module
import turtle
from turtle import Screen

# create a turtle object
t = turtle.Turtle()
t.speed("fastest")

# set the shape and color of the turtle
t.shape("turtle")
t.color("black")

# define a function to move the turtle to a given position
def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# define a function to draw a circle with a given radius and angle
def draw_circle(radius, angle):
    t.circle(radius, angle)

# define a function to draw a feather with a given color and size
def draw_feather(color, size):
    # set the fill color
    t.fillcolor(color)
    # start filling
    t.begin_fill()
    # draw the outer arc
    draw_circle(size, 90)
    draw_circle(size / 3, 80)
    draw_circle(size * 2, 50)
    # draw the inner arc
    t.left(180)
    draw_circle(size * 2, 50)
    draw_circle(size / 3, 80)
    draw_circle(size, 90)
    # end filling
    t.end_fill()

# draw the left down feather
go(-130, -50)
t.setheading(-130)
draw_feather("yellow", 130)
go(-110, -50)
t.setheading(-130)
draw_feather("red", 120)

# draw the right down feather
go(140, -50)
t.setheading(-50)
draw_feather("yellow", -130)
go(120, -50)
t.setheading(-50)
draw_feather("red", -120)

# draw the right upper feather
go(0, -70)
t.setheading(-20)
t.fillcolor("yellow")
t.begin_fill()
draw_circle(220, 45)
draw_circle(50, 60)
draw_circle(-120, 40)
draw_circle(50, 160)
draw_circle(250, 60)
t.end_fill()
go(150, 90)
t.setheading(-150)
t.fillcolor("red")
t.begin_fill()
draw_circle(90, 40)
draw_circle(30, 140)
draw_circle(90, 40)
draw_circle(30, 140)
t.end_fill()
go(145, 70)
t.setheading(-150)
t.fillcolor("yellow")
t.begin_fill()
draw_circle(40, 40)
draw_circle(20, 140)
draw_circle(40, 40)
draw_circle(20, 140)
t.end_fill()

# draw the left upper feather
go(10, -75)
t.setheading(-160)
t.fillcolor("yellow")
t.begin_fill()
draw_circle(-220, 45)
draw_circle(-50, 60)
draw_circle(120, 40)
draw_circle(-50, 160)
draw_circle(-250, 60)
t.end_fill()
go(-150, 90)
t.setheading(-30)
t.fillcolor("red")
t.begin_fill()
draw_circle(-90, 40)
draw_circle(-30, 140)
draw_circle(-90, 40)
draw_circle(-30, 140)
t.end_fill()
go(-145, 75)
t.setheading(-30)
t.fillcolor("yellow")
t.begin_fill()
draw_circle(-40, 40)
draw_circle(-20, 140)
draw_circle(-40, 40)
draw_circle(-20, 140)
t.end_fill()

# draw the body
t.fillcolor("red")
go(-20, -80)
t.setheading(-120)
t.begin_fill()
draw_circle(90, 70)
draw_circle(-70, 40)
t.setheading(90)
draw_circle(-70, 40)
draw_circle(90, 70)
t.end_fill()

# draw the head
t.fillcolor("yellow")
go(-13, -90)
t.setheading(-27)
t.begin_fill()
draw_circle(40, 60)
draw_circle(30, 120)
draw_circle(40, 60)
draw_circle(30, 120)
t.end_fill()
go(-10, -30)
t.setheading(-27)
t.begin_fill()
draw_circle(30, 60)
draw_circle(20, 120)
draw_circle(30, 60)
draw_circle(20, 120)
t.end_fill()

# draw the eyes
t.fillcolor("white")
# left eye
go(10, 30)
t.setheading(-120)
t.begin_fill()
draw_circle(30, 60)
draw_circle(15, 120)
draw_circle(30, 60)
draw_circle(15, 120)
t.end_fill()
t.fillcolor("black")
go(20, 20)
t.begin_fill()
t.circle(8)
t.end_fill()
t.pencolor("white")
t.fillcolor("white")
go(18, 18)
t.begin_fill()
t.circle(3)
t.end_fill()
# right eye
t.pencolor("black")
go(-25, 30)
t.setheading(-120)
t.begin_fill()
draw_circle(30, 60)
draw_circle(18, 120)
draw_circle(30, 60)
draw_circle(18, 120)
t.end_fill()
t.fillcolor("black")
go(-15, 20)
t.begin_fill()
t.circle(10)
t.end_fill()
t.pencolor("white")
t.fillcolor("white")
go(-15, 12)
t.begin_fill()
t.circle(4)
t.end_fill()

# draw the antenna
t.pencolor("black")
go(6, 30)
t.setheading(90)
draw_circle(60, 50)
draw_circle(10, 180)
draw_circle(5, 160)
go(10, 30)
t.setheading(80)
draw_circle(-60, 55)
draw_circle(-10, 180)
draw_circle(-5, 160)

# hide the turtle
t.hideturtle()


screen = Screen()
screen.exitonclick()