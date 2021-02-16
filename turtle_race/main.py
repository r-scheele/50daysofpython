from turtle import Turtle, Screen
from random import randint

screen = Screen()

is_race_on = False
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_position = 0
all_turtles = []
for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)

    turtle.penup()
    turtle.goto(x=-230, y=-100 + turtle_position)
    turtle_position += 50
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} is the winner!")

        turtle.forward(randint(0, 10))

screen.exitonclick()
