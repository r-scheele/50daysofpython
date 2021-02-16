import turtle
from random import randint, choice

turtle.colormode(255)

turtle = turtle.Turtle()

angles = [0, 90, 180, 270]
turtle.pensize(10)
turtle.speed('fastest')

for _ in range(200):
    turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))
    turtle.forward(30)
    turtle.setheading(choice(angles))


