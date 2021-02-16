import turtle as t
from random import randint

t.colormode(255)
turtle = t.Turtle()

turtle.speed('fastest')


def draw_spiro(gap_size):
    for i in range(int(360 / gap_size)):
        turtle.color((randint(0, 255), randint(0, 255), randint(0, 255)))
        turtle.circle(100)
        turtle.setheading(turtle.heading() + gap_size)


draw_spiro(5)

t.Screen().exitonclick()
