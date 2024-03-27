from turtle import *
from colorsys import *
import turtle
import time


# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

bgcolor('black')
tracer (1000)
pensize (1)
h = 0

def draw(ang, n):
    circle(5+n, 69)
    left(ang)
    circle(5+2*n, 60)

goto (0,0)

for i in range(5000):
    c = hsv_to_rgb(h, 1, 1)
    h += 0.005
    color(c)
    up()
    draw(90, i)
    # draw(270, i)
    down()
    draw(180, i)
    # draw(360, i)
    time.sleep(0.05)  # Slow down the execution
    