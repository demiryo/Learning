import turtle

def HelloWorld(fred):
    fred.shape("turtle")
    fred.color("green")
    fred.pencolor("brown")
    fred.forward(200)
    fred.circle(100)
    fred.circle(-100)
    fred.forward(200)

def DrawHeart(fred):
    fred.shape("turtle")
    fred.color("green")
    fred.pencolor("brown")
    '''
    fred.penup()
    fred.right(90)
    fred.forward(130)
    fred.right(180)
    fred.pendown()
    fred.circle(120, 180, 20)
    fred.circle(-120, -180, 20)
    '''
    fred.right(90)
    fred.circle(120, -180, 20)
    fred.circle(-120, 180, 20)
    fred.right(30)
    fred.forward(400)
    fred.right(470)
    fred.forward(450)


myTurtle = turtle.Pen()
# Call HelloWorld function
#HelloWorld(myTurtle)
DrawHeart(myTurtle)
turtle.done()