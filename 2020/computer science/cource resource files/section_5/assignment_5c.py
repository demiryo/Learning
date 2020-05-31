from turtle import*

speed(0)

width(10)

print("first shape")

for i in range(4):
    right(90)
    circle(200, steps= 4) #square


input("press enter to continue.. ")

input("are you sure you are ready?")
print("  =)   ")

from random import randint # random colors import needed


width(0)  # below creates random colors for the surprise. 
bgcolor('black')
x = 1
while x < 450:
 
 r = randint(0,255)
 g = randint(0,255) 
 b = randint(0,255)
 
 colormode(255) 
 pencolor(r,g,b)
 fd(60 + x)
 rt(61)
 x = x+1


print("crazy art!!")

print("please click on the window exactly in order to exit properly")

exitonclick()

exit #this solves a bug for some reason
