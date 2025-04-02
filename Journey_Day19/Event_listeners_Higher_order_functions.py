
from turtle import Turtle , Screen
tim=Turtle()
screen=Screen()


def move_forwards():
    tim.forward(100)

screen.listen()
screen.onkey(key="space",fun=move_forwards)
screen.exitonclick()

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

def calculator(n1,n2,func):
    return func(n1,n2)

result=calculator(2,3,divide)
print(result)

