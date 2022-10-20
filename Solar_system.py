'''
CREATING A SOLAR SYSTEM USING TURTLE MODULE
APPROACH: 1. Import required packages.
          2. Create a screen in which we can place planets.
          3. Create sun (sun is in center. sngle and radius not required).
          4. Create planet Class.
        4.1. Define name, radius and color function.
        4.2. Define movement in radius and angles (sine and cosine).
          5. Create Planets with name, radius and color.
          6. Append planet details to a list.
          7. Make the planets move.

'''


import turtle
import time
from math import *

screen = turtle.Screen()
screen.tracer(500)

# making sun

sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')


class Planet(turtle.Turtle):
    def __init__(self, name, radius, color):
        super().__init__(shape = 'circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0

    def move(self):
        x = self.radius * cos(self.angle)
        y = self.radius * sin(self.angle)

        self.goto(sun.xcor() + x, sun.ycor() + y)


# Creating Planets
#Planet(name, radius, color)

mercury = Planet("Mercury", 40, 'grey')
venus = Planet("Venus", 80, 'orange')
earth = Planet("Earth", 100, 'blue')
mars = Planet("Mars", 130, 'maroon')
jupiter = Planet("Jupiter", 200, 'brown')
saturn = Planet("Saturn", 250, 'pink')
uranus = Planet("Uranus", 290, 'light blue')
neptune = Planet("Neptune", 320, 'black')

# adding planets to list 

planets_list = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

# Moving planets

while True:
    screen.update()
    for i in planets_list:
        i.move()

# (angle in radians)

    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007
    jupiter.angle += 0.02
    saturn.angle += 0.018
    uranus.angle += 0.016
    neptune.angle += 0.005

