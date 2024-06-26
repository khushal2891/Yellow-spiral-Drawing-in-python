import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)  # Set screen dimensions
screen.bgcolor('black')  # Set background color

# Create a turtle object
t = turtle.Turtle()
t.speed(0)  # Set the speed of the turtle

# Define colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

# Draw a spiral
for i in range(360):
    t.pencolor(colors[i % 6])  # Cycle through the colors
    t.width(i/100 + 1)  # Increase the width of the pen
    t.forward(i)
    t.left(59)

# Hide the turtle
t.hideturtle()

# Keep the window open
screen.mainloop()