from turtle import*

#variables

def get_input_or_default(input_message, defalt_value ):
    """
    this function will take an input message and a defalt value 
    and will ask the user to enter the value or else use the defalt 
    """
    input_value = input(input_message).strip()
    if input_value == "":
        return defalt_value
    return input_value 

#inputs for all values
space_width = int(get_input_or_default("enter a number for how wide the space bitween the letters [default: 35] : ", 35)) 
letter_height = int(get_input_or_default("enter a number for the letter height [default: 100] : ", 100)) 
letter_width = int(get_input_or_default("enter a number for the letter width (recomend half of height [default: 50] ) : ", 50)) 
pen_color = get_input_or_default("enter a color [default: green] : ", "green") 
pen_width = int(get_input_or_default("enter a number for the thickness [default: 10] : ", 10)) 


def start_pos(): 
    #start position
    penup()
    goto(-200,100) 
    pendown()

def _indent():
    penup()
    goto(-200,-letter_height) 
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
    forward(space_width)
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

    letter_o()

    _space()



color(pen_color) 
width(pen_width)

make_hello()

make_world()

exitonclick() 
