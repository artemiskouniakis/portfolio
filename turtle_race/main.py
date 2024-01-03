from turtle import Turtle, Screen
import random


is_race_on = True

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your Bet!", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_placement = -100

rivals = []

for color in colors:
    rival = Turtle(shape="turtle")
    rival.color(color)
    rival.penup()
    rival.goto(x= -240, y=y_placement)
    y_placement = y_placement + 40
    rivals.append(rival)

if user_bet:
    is_race_on = True

while is_race_on:
    rival_index = random.randint(0,5)
    rand_dist = random.randint(0,10)
    rivals[rival_index].forward(rand_dist)
    if rivals[rival_index].xcor() >= 225:
        is_race_on = False
        winner = colors[rival_index]

if user_bet == winner:
    print(f"{winner} is on 1st place. You Won!")
else:
    print(f"{winner} is on 1st place. You lost...")



screen.exitonclick()