from turtle import *

"""
The program has three turtle buttons, shaped like a red circle, a blue square,
and a green triangle. (3.0 pts)

_____ When the user clicks each button, the unnamed turtle changes to
that color and shape and then draws a shape in that color. (6.0 pts)
_____ The user can click and drag the unnamed turtle to draw with it.
TIP: It’s okay if this feature is a little buggy. (1.0 pts)
_____ The program includes a docstring at the top that describes how to use the program.
(1.0 pts)
_____ The screen resets when the user presses the SPACEBAR key.
TIP: The lines go away and the unnamed turtle returns to the center.
It doesn’t return to the original turtle color and shape. (1.0 pts
"""

class Shape(Turtle):
    def __init__(self, icolor, shape_name, x, y, isize):
        super(Shape, self).__init__()
        self.shape_name = shape_name
        self.icolor = icolor
        self.size=isize
        self.color(icolor)
        self.penup()
        self.goto(x, y)
        self.onclick(self.on_click_handler)
        self.shape(self.shape_name)

    def on_click_handler(self, x, y):
        print("click on = {0}, {1}".format(x,y))
        self.penup()
        self.goto(x, 100) # just give room to draw the shape
        self.Draw()
        self.penup()
        self.goto(x, -45)
        
class Square(Shape):
    def __init__(self, icolor, x, y, isize):
        super(Square, self).__init__(icolor, "square", x, y, isize)

    def Draw(self):
        color(self.icolor)
        fillcolor(self.icolor)
        begin_fill()
        right(45)
        circle(self.size, steps=4)
        end_fill()
        left(45)
        
class Circle(Shape):
    def __init__(self, icolor, x, y, isize):
        super(Circle, self).__init__(icolor, "circle", x, y, isize)

    def Draw(self):
        color(self.icolor)
        fillcolor(self.icolor)
        begin_fill()
        circle(self.size)
        end_fill()
        
class Trangle(Shape):
    def __init__(self, icolor, x, y, isize):
        super(Trangle, self).__init__(icolor, "triangle", x, y, isize)

    def Draw(self):
        color(self.icolor)
        fillcolor(self.icolor)
        begin_fill()
        right(60)
        circle(self.size, steps = 3)
        end_fill()
        left(60)
"""
def redraw():
    clear()
    listen()
    myBlueSquare = Square(icolor="blue", x=50, y=0, isize=50)
    myRedCircle = Circle(icolor="red", x=100, y=0, isize=35)
    myGreenTrangle = Trangle(icolor="green", x=150, y=0, isize=50)
        
onkey(redraw(), "space")  having trouble
listen()
"""


myBlueSquare = Square(icolor="blue", x=50, y=0, isize=50)
myRedCircle = Circle(icolor="red", x=100, y=0, isize=35)
myGreenTrangle = Trangle(icolor="green", x=150, y=0, isize=50)

#onkey(clear(), "spacebar")   i am having trouble with this part
    
#listen()   i wrote this program from scratch with help of online tools..

# i am hoping this will count for some extra credit

#redraw()  


        


mainloop()
