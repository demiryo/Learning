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

def _indent():
    penup()
    goto(-200,-letter_height) 
    pendown()

def letter_r():
    # letter R

    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    right(90)
    forward(letter_width)
    right(90)
    forward(letter_width)
    left(135)
    forward(letter_height * 0.75)
    left(45)

def letter_w():
    # letter w

    left(90)
    forward(letter_height)
    back(letter_height)
    right(90)
    forward(letter_width/2)
    left(90)
    forward(letter_width)
    back(letter_width)
    right(90)
    forward(letter_width/2)
    left(90)
    forward(letter_height)
    back(letter_height)
    right(90)

def letter_d():
    # letter O

    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    right(60)
    forward( 0.6 * letter_height)
    right(60)
    forward( 0.6 * letter_height)
    right(60)
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

def make_world():
    #making W O R L D
    _indent()

    letter_w()

    _space()

    letter_o()

    _space()

    letter_r()

    _space()

    letter_l()

    _space()

    letter_d()

    _space()


#width(pen_width)

speed(0)
    
for A in range(10):
    make_hello()
    make_world()
    width(A)
    right(A)
    

    

exitonclick() 
