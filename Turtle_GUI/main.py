from turtle import Turtle, Screen
import turtle as t
import math
import random


timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
t.colormode(255)
#timmy_the_turtle.color("#ba5757")




def draw_square(timmy_the_turtle):
    for times in range(0,4):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(90)

def draw_triangle(timmy_the_turtle):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(135)
    hypotenuse = pow(100,2) + pow(100,2)
    timmy_the_turtle.forward(math.sqrt(hypotenuse))
    

def draw_random_path(timmy_the_turtle):
    corners = [45*2, 45*4, 45*6, 45*8]
    for _ in range(1,100):
        timmy_the_turtle.forward(50)
        timmy_the_turtle.pencolor((random.choice(range(1,255))),(random.choice(range(1,255))),(random.choice(range(1,255))) )
        timmy_the_turtle.right(random.choice(corners))
        
        
def draw_circle(timmy_the_turtle):
    timmy_the_turtle.speed("fastest")
    for _ in range(1,int(360/10)):
        timmy_the_turtle.pencolor((random.choice(range(1,255))),(random.choice(range(1,255))),(random.choice(range(1,255))) )
        timmy_the_turtle.circle(100)
        current_heading = timmy_the_turtle.heading()
        timmy_the_turtle.setheading(current_heading + 10)
        



#draw_square(timmy_the_turtle)
#timmy_the_turtle.left(90)
#draw_triangle(timmy_the_turtle)
#draw_random_path(timmy_the_turtle)
draw_circle(timmy_the_turtle)

screen = Screen()
screen.exitonclick()