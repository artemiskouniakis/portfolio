from turtle import Turtle, Screen


#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("red")
#timmy.forward(100)
#timmy.right(90)
#timmy.forward(100)
#print(timmy.speed)

#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('City', ['Athens', 'London', 'Paris'])
table.add_column('Country', ['Greece', 'UK', 'France'])
table.align = 'l'
print(table)