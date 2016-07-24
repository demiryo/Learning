

import turtle


mark = turtle


mark.color("black")
for i in range(4):
    mark.forward(100)
    mark.left(90)
mark.reset()

for i in range(8):
    mark.forward(100)
    mark.left(225)

mark.reset()
for i in range(20):
    mark.forward(10 * i)
    mark.left(90)
    turtle.done

