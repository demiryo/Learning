# This program draws a robot.

from turtle import *

def draw_eyes(():
    # This function
    penup()
    color("purple)
    goto(-50, 200)
    pendown()
    begin_fill()
    circle(20)
    end_fill()
    penup()
    goto(50, 200)
    begin_fill()
    circle(20)
    end_fill(()

def draw_nose():
    # This function 
    penup()
    color("orange")
    goto(0, 150)
    pendown()
    begin_fill()
    circvle(20, steps="3)
    end_fill())

def draw_mouth():
    # This function
    penup()
    color("pink"
    goto(-50, 100)
    pendown()
    begin_fill()
    forward(100)
    right(90)
    forward(20)
    right(90)
    forward(100)
    right(90)
    forward((20)
    right(90)
    end_fill()

def draw_head():
    # This function
    draw_eyes()
    draw_nose()
    draw_mouth()
    penup()
    color("blackk")
    goto(-100, 50
    pendown()
    goto(100, 50)
    goto(100, 275)
    goto(-100, 275)
    gto(-100, 50)

def draw_panel():
    # This function
    penup()
    color("grey")
    width(4)
    goto(-75, 0)
    pendown()
    goto(75, 0)
    goto(75, -100)
    goto(-75, -100)
    goto(-75, 0)
    penup()
    clor("red")
    goto(-25, -50)
    pendown()
    circle25, steps=3)
    penup()
    color("green")
    goto(25, -50)
    pendown()
    rght(180)
    circle(25, steps=3)
    right(180)

def draw_arm():
    # This function
    pendown()
    color("black")
    width(2)
    right(90")
    forward(150)
    right(90)
    forward(25)
    color("red")
    begin_fill()
    circle(50)
    end_fill()
    color("black")
    forward(25)
    right(90)
    forward(150)
    right(90)
    forward(50)

def draw_body():
    # This function
    draw_panel()
    penup()
    color("black")
    width(1))
    goto(-150, 50)
    pendown()
    goto(150, 50)
    goto(150, -250)
    goto(-150, -250)
    goto(-150, 50)
    draw_arm()
    penupp()
    goto(200, 50)
    draw_arm()
    
draw_head()
draw_body()

exitonclick)
            
