# import turtle
from colorsys import hsv_to_rgb
import random
import turtle

# Generate random color
def random_color():
    r, g, b = [int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1)]
    return f"#{r:02x}{g:02x}{b:02x}"

# setup turtle pen
t= turtle.Pen()

# changes the speed of the turtle
t.speed(10)

# changes the background color
turtle.bgcolor("black")

size = 500

# make spiral_web
for x in range(size):
    twidth = x % 3
    t.pencolor(random_color()) # setting color
    t.width(twidth) # setting width
    t.forward(x) # moving forward
    t.left(59) # moving left

turtle.done()
t.speed(10)

turtle.bgcolor("black") # changes the background color

# make spiral_web
for x in range(size):
    twidth = x % 3
    t.pencolor(random_color()) # setting color
    t.width(twidth) # setting width
    t.forward(x) # moving forward
    t.left(59) # moving left

turtle.done()