from turtle import*

#variables



space_Width = 30 # for value 30

letter_height = 100 # for value 100

letter_width = 50 # for value 50

pen_color = input("enter a color __ ")

#pen_width = input("enter a number for the width __ ")

def start_pos(): 
    #start position
    penup()
    goto(-200,100) 
    pendown()
    
def letter_h():
    # letter H

    left(90)
    forward(letter_height)
    back(letter_width)
    right(90)
    forward(letter_width)
    left(90)
    forward(letter_width)
    back(letter_height)
    right(90)
    
def _space():
    # space
    penup()
    forward(space_Width)
    pendown()

def letter_e():
    # letter E

    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    back(letter_width)
    left(90)
    back(letter_width)
    right(90)
    forward(letter_width)
    back(letter_width)
    left(90)
    back(letter_width)
    right(90)
    forward(letter_width)

def letter_l():
    # letter L

    left(90)
    forward(letter_height)
    back(letter_height)
    right(90)
    forward(letter_width)

def letter_o():
    # letter O

    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    right(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    left(180)
    forward(letter_width)

def make_hello():
    #making H E L L O
    start_pos()

    color(pen_color)

    letter_h()

    _space()

    letter_e()

    _space()

    letter_l()

    _space()

    letter_l()

    _space()

    letter_o()

    _space()



#width(pen_width)

speed(0)
    
for i in range(10):
    make_hello()
    width(i)
    right(i*3)
    

    

exitonclick() 
