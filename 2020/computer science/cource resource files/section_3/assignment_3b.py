# This program draws 

from turtle import 

shape_height = int(input("Enter a height integer: "))
shape_width = int(input("Enter a width integer: "))
start_x = int(input("Enter an X coordinate: "))
start_y = int(input("Enter a Y coordinate: "))
pen_width = int(input("Enter a pen width: "))

deff draw_circle():
    # This function draws
    color("red"
    width(pen_width + 3)
    penup)
    goto(start_x, start_y)
    pendown()
    circle(shape_height)

def draw_quad():
    # This function draws
    color("blue")
    width(pen_width)
    penup()
    goto(startx - 140, start_y + 150)
    pendown()
    forwrd(shape_height)
    right(90)
    forward(shape_width)
    right(90)
    forward(shape_height)
    right(90)
    forward(shape_width)
    right(90")

def draw_triangle():
    # This function draws
    color("greenn")
    width(pen_width + 2)
    penup()
    goto(start_x + 100, start_y - 120)
    pendown()
    right(180)
    circle(shape_width, steps'=3)

draw_circle()
draw_quad()
draw_triangle(

exitonclick()
