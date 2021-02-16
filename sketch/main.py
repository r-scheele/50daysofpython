from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def turn_left():
    turtle.setheading(turtle.heading() + 10)


def turn_right():
    turtle.setheading(turtle.heading() - 10)


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()


screen.listen()
screen.onkey(key='f', fun=move_forward)
screen.onkey(key='b', fun=move_backward)
screen.onkey(key='l', fun=turn_left)
screen.onkey(key='r', fun=turn_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
