from turtle import Turtle, Screen
import random

turtle = Turtle()


class Solids:
    def __init__(self, highest, orientation):
        self.number_of_sides = 3
        self.angle = 360 / self.number_of_sides
        self.highest_shape = highest
        self.orientation = orientation
        self.colors = ['CornFlowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat']

    def move(self, curve_angle):
        turtle.forward(100)
        turtle.left(curve_angle) if self.orientation == 'up' else turtle.right(curve_angle)

    def draw(self):
        while self.number_of_sides < self.highest_shape + 1:
            turtle.color(random.choice(self.colors))
            for _ in range(self.number_of_sides):
                self.move(self.angle)
            self.number_of_sides += 1
            self.angle = 360 / self.number_of_sides


solid = Solids(10, 'up')
solid.draw()

screen = Screen()
screen.exitonclick()
