

import turtle


mark = turtle

# -----------------------------------------------
# Draw a rectangle
# -----------------------------------------------
mark.color("black")
for i in range(4):
    mark.forward(100)
    mark.left(90)
mark.reset()

# -----------------------------------------------
# draw a 16 side star
# -----------------------------------------------

for i in range(8):
    mark.forward(100)
    mark.left(225)
mark.reset()

# -----------------------------------------------
# cubed sea shell
# -----------------------------------------------

for i in range(20):
    mark.forward(10 * i)
    mark.left(90)
mark.reset()

# -----------------------------------------------
# sea shell
# -----------------------------------------------


for i in range(50):
    mark.circle(i * 3)
    mark.left(10)
mark.reset()

# -----------------------------------------------
# rose
# -----------------------------------------------

for i in range(30):
    mark.circle(i*3, 180)
    mark.right(45)
mark.reset()

# -----------------------------------------------
# swerly piramid
# -----------------------------------------------



for i in range(100):
    mark.forward(i*2)
    mark.circle(i*2, 90)
    mark.right(20)
mark.reset()


# -----------------------------------------------
# swerly spikes
# -----------------------------------------------

for i in range(154):

    mark.circle(i*5, 75)
    mark.forward(i*3)
    mark.left(25)

turtle.done