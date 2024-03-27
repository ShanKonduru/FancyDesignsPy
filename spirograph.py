import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Define the number of circles and the radius increment
num_circles = 500
radius_increment = 3
line_width = 3  # Set the line width

# Function to draw concentric circles
def draw_concentric_circles(num_circles, radius_increment):
    for i in range(num_circles):
        # Randomize line color
        color = (random.random(), random.random(), random.random())  # RGB tuple
        t.pencolor(color)
        
        # Set line width
        t.width(line_width)
        
        # Draw circle
        t.penup()
        t.goto(0, -i * radius_increment)
        t.pendown()
        t.circle(i * radius_increment)

# Draw concentric circles
draw_concentric_circles(num_circles, radius_increment)

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed manually
screen.mainloop()
