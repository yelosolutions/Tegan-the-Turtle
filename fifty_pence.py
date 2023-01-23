import turtle

def draw_fifty_pence(n):
    # Set up turtle
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    #turtle.color(color)
    # Draw n fifty pence shapes
    for i in range(n):
        # Draw 7 sides of the shape
        for j in range(7):
            turtle.forward(50)
            turtle.left(360/7)

        # Move turtle to next position
        turtle.penup()
        turtle.forward(150)
        turtle.pendown()

# Ask user for input
num_coins = int(input("Enter the number of fifty pence shapes to draw: "))
#color = input("Enter the color of the shape: ")

# Draw the shapes
draw_fifty_pence(num_coins)

# Keep the turtle window open
turtle.mainloop()