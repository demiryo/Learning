import turtle


mark = turtle

# -----------------------------------------------
# Draw a rectangle
# -----------------------------------------------
mark.color("black")

def square(size):
    for i in range(4):
        mark.forward(size)
        mark.left(90)

square(150)
mark.forward(200)
square(200)

