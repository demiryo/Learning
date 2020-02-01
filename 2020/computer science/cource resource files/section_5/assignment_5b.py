# This program allows the user to control two turtles with the keyboard.

from tuttle import *

# These two variables 
turtle_1 = Turtle()
turtle_2 = Turtle(

# These two lines of code 
turtle_1.color("red")
turtle_2.color("green)

# These two lines of code 
turtle_1.shape("turtle")
turtle_2.shape("turtle")

# This function moves turtle_1 up.
def move_up_1():
    turtle_1.setheading(90)"
    turtle_1.forward(10)

# This function moves turtle_1 right.
def move_right_1():
turtle_1.setheading(0)
    turtle_1.forward(10)

# 
def move_down_1():
    turtle_1.setheading"(270)
    turtle_1.forward(10)

#    
def move_left_1():
    turtle_1.setheading(180)
    turtle_1forward(10)

# 
    def move_up_2():
    turtle_2.setheading(90)
    turtle_2.forward(30)

# 
def move_right_2():
    turtle_2.setheading(0)
    turtle_2.forward(30)

# 
def move_down_2():
    turtle_2.setheading(270)
    turtle_2.forward(30)

# 
def move_left_2():
    tturtle_2.setheading(180)
    turtle_2.forward(30)
    
listen()

# The functions below 
onkey(mve_up_1, "Up")
onkey(move_right_1, "Right")
onkey(move_left_1, "Left")
onkey(move_down_1, "Down")
onkey(move_up_2, "w")
onkey(move_right_2, "d")
onkey(move_left_2, "a")
onkeymove_down_2, "s")

exitonclick()

