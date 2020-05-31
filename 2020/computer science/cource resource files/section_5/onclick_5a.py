from turtle import *


class Shape(Turtle):
    def __init__(self, icolor, isize):
        self.color = icolor
        self.size = isize
        super(Shape, self).__init__()

    def Draw(self):
        raise RuntimeError("Can't call base class, must override draw")

class Square(Shape):
    def __init__(self, icolor, isize):
        super(Square, self).__init__(icolor, isize)
        
    def Draw(self):
        color(self.color)
        fillcolor(self.color)
        begin_fill()
        right(45)
        circle(self.size, steps=4)
        end_fill()
        left(45)

class Circle(Shape):
    def __init__(self, icolor, isize):
        super(Circle, self).__init__(icolor, isize)
 
    def Draw(self):
        color(self.color)
        fillcolor(self.color)
        begin_fill()
        circle(self.size)
        end_fill()

class Trangle(Shape):
    def __init__(self, icolor, isize):
        super(Trangle, self).__init__(icolor, isize)
 
    def Draw(self):
        color(self.color)
        fillcolor(self.color)
        begin_fill()
        right(60)
        circle(self.size, steps = 3)
        end_fill()
        left(60)

def skip(step=150):
    penup()
    forward(step)
    pendown()

        
myBlueSquare = Square(icolor="blue", isize=50)
myBlueSquare.Draw()

skip()

myRedCircle = Circle(icolor="red", isize=35)
myRedCircle.Draw()

skip(100)

myGreenTrangle = Trangle(icolor="green", isize=50)
myGreenTrangle.Draw()


mainloop()
