from turtle import *
from colorsys import *
import random

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Beautiful Flower Design")

# Initialize Turtle
t = Turtle()
t.speed(0)
t.hideturtle()

# List to store flower positions
flower_positions = []

# Define function to draw a petal
def draw_petal(radius, color1, color2):
    t.color(color1, color2)
    t.begin_fill()
    t.circle(radius, 60)
    t.left(120)
    t.circle(radius, 60)
    t.left(120)
    t.end_fill()

# Define function to draw a flower
def draw_flower(x, y, petals, radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(petals):
        draw_petal(radius, random_color(), random_color())
        t.left(360 / petals)

# Generate random color
def random_color():
    r, g, b = [int(x * 255) for x in hsv_to_rgb(random.random(), 1, 1)]
    return f"#{r:02x}{g:02x}{b:02x}"

# Draw multiple flowers without overlapping
def draw_flowers():
    for _ in range(12):
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        while is_overlapping(x, y):
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
        petals = random.randint(5, 10)
        radius = random.randint(50, 100)
        draw_flower(x, y, petals, radius)
        flower_positions.append((x, y))

# Function to check if a flower overlaps with existing ones
def is_overlapping(x, y):
    for pos_x, pos_y in flower_positions:
        distance = ((pos_x - x) ** 2 + (pos_y - y) ** 2) ** 0.5
        if distance < 150:  # Adjust this threshold as needed
            return True
    return False

# Draw flowers without overlapping
draw_flowers()

# Hide Turtle
t.hideturtle()

# Keep the window open
screen.mainloop()
