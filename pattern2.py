import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")
screen.title("Star Pattern")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.hideturtle()

# Function to draw a star
def draw_star(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    for _ in range(5):
        pen.forward(50)
        pen.right(144)

# Draw stars at specific coordinates
draw_star(-100, 100)
draw_star(0, 150)
draw_star(100, 100)
draw_star(0, 50)
draw_star(100, 0)
draw_star(-100, 0)
draw_star(0, -50)
draw_star(150, -150)
draw_star(-150, -150)
draw_star(-200, 0)
draw_star(200, 0)
draw_star(0, 200)

# Keep the window open until closed manually
turtle.done()
