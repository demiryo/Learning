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
    fred.circle(120, 180, 10)

myTurtle = turtle.Pen()
# Call HelloWorld function
#HelloWorld(myTurtle)
DrawHeart(myTurtle)
turtle.done()