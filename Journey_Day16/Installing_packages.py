from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)


my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

my_screen_2=Screen()
print(my_screen.canvheight)
my_screen_2.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
print(table)

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)

table.align="l"

print(table)

