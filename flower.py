from turtle import *
from colorsys import *
import random

bgcolor('black')
tracer (100)
pensize (2)
h = 0

def draw(ang, n):
	circle (5+n, 69) # random.randint(65, 69))
	left (ang)
	circle(5+2*n, 60) # random.randint(55, 60))

goto (0,0)

for i in range(5000):
	c = hsv_to_rgb(h, 1, 1)
	h += 0.005
	color (c)
	up()
	draw(90, i)
	draw(180, i)
	down()
	draw (1/2, i-1)
	draw(180, i/2)
	draw (120, i-1)
