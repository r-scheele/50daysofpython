import turtle as t
from random import choice

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)

colors = [
    (225, 229, 236), (242, 236, 219), (243, 233, 241), (231, 242, 236), (191, 165, 119), (139, 167, 191),
    (142, 93, 47), (53, 103, 144), (222, 207, 121), (9, 20, 54), (187, 157, 31), (56, 16, 6), (184, 149, 168),
    (143, 178, 154), (71, 119, 81), (57, 11, 23), (129, 77, 101), (10, 34, 18), (20, 47, 133), (138, 24, 12),
    (179, 187, 216), (168, 101, 133), (124, 25, 43), (96, 153, 99), (212, 177, 197), (173, 205, 180),
    (94, 121, 178), (21, 93, 59), (65, 153, 171), (90, 78, 13), (175, 103, 93), (219, 179, 174), (234, 207, 8),
    (14, 86, 100), (161, 203, 212)
]
turtle.hideturtle()
turtle.speed('fastest')
screen.setup(width=800, height=800)
turtle.penup()
turtle.goto(x=-300, y=-300)
turtle.pendown()


def make_painting(space, dimension):
    for y in range(dimension):
        for x in range(dimension):
            turtle.penup()
            turtle.dot(20, choice(colors))
            turtle.forward(space)

        turtle.left(90)
        turtle.forward(space)
        turtle.left(90)
        turtle.forward(space * dimension)
        turtle.right(90)
        turtle.forward(space)
        turtle.right(90)


make_painting(40, 10)

t.Screen().exitonclick()
