from turtle import *

#this program draws a sword 



def handle_s():
    # this makes the handle
    
    color("black")
    width(3)
    forward(20)
    right(90)
    forward(60)
    right(90)
    forward(20)
    right(90)
    forward(20)
    right(90)
    width(5)
    forward(20)
    back(20)
    width(3)
    left(90)
    forward(20)
    right(90)
    width(5)
    forward(20)
    back(20)
    width(3)
    left(90)
    forward(20)
    right(90)
    width(5)
    forward(20)
    back(20)
    width(3)
    left(180)

def guard_s():
    #this makes the hand guard

    color("#8B4513")
    forward(30)
    right(90)
    forward(10)
    right(90)
    forward(80)
    right(90)
    forward(10)
    right(90)
    forward(30)
    width(5)
    forward(20)
    width(3)
    back(50)
    left(90)
    back(10)
    right(90)
    forward(30)
    right(90)

def blade_s():
    #this makes the blade

    color("#808080")
    width(2)
    forward(150)
    left(15)
    forward(30)
    right(195)
    forward(155)
    width(5)
    forward(20)
    width(2)
    back(175)
    right(15)
    forward(30)
    left(15)
    forward(150)

def turtle_goAway():
    #get turtle icon away

    penup()
    goto(1000,200)

handle_s()
guard_s()
blade_s()
turtle_goAway()

exitonclick()
