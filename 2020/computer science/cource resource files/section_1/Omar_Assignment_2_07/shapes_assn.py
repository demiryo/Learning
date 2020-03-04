from turtle import *

shape("turtle")

#this is used to increase turtle speed
speed(10)

# black square
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

# to face the turtle up
left(90)

# blue circle
color("blue")
circle(100)

# green square
color("green")
circle(100, steps=4)

# red triangle
color("red")
circle(100, steps=3)

# other red triangle
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)




exitonclick()
