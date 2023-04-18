import turtle

# Initialize the turtle and set the background color
t = turtle.Turtle()
turtle.bgcolor("black")

# Set the pen size and speed
t.pensize(3)
t.speed(0)

# Create a list of rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw a rainbow spiral
for x in range(100):
    t.pencolor(colors[x % 7])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(50)

# Hide the turtle
t.hideturtle()

turtle.done()
