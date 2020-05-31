from turtle import*

speed(0)

color("blue")

width(3)


for i in range(26):
    for i in range(4):
        circle(200, steps=6)
        right(1)
    
    right(10)
    forward(5)




exitonclick() 

# THIS IS EXTRAS,
#UNCOMMENT TO SEE THAT BLACK VOID ROMBUS I TALKED ABOUT IN THE CLASS

#  right(2)
#  forward(2)

#import msvcrt as m
#def wait():
#    m.getch()

#wait()
#input("Press Enter to continue...")

#clear()


#color("black")

#width(1)

#for i in range(106):
#    for i in range(4):
#        circle(200, steps=4)
#        right(1)
    
#    right(10)

#wait()
#input("Press Enter to continue...")

#print("this takes longer")

#for i in range(150):
#    for i in range(4):
#        circle(200, steps=7)
#        right(1)
    
#    right(10)

#wait()
#input("Press Enter to continue...")

#print("this takes longer too")

#for i in range(150):
#    for i in range(4):
#        circle(200, steps=6)
#        right(1)
    
#    right(10)
