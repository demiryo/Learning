from turtle import*

def start_pos(): 
    #start position
    penup()
    goto(-200,100) 
    pendown()
    
def letter_h():
    # letter H

    left(90)
    forward(100)
    back(50)
    right(90)
    forward(50)
    left(90)
    forward(50)
    back(100)
    right(90)
def _space():
    # space
    penup()
    forward(30)
    pendown()

def letter_e():
    # letter E

    left(90)
    forward(100)
    right(90)
    forward(50)
    back(50)
    left(90)
    back(50)
    right(90)
    forward(50)
    back(50)
    left(90)
    back(50)
    right(90)
    forward(50)

def letter_l():
    # letter L

    left(90)
    forward(100)
    back(100)
    right(90)
    forward(50)

def letter_o():
    # letter O

    left(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    right(90)
    forward(50)
    left(180)
    forward(50)

def make_hello():
    #making H E L L O
    start_pos()

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

make_hello()

exitonclick() 
