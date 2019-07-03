import random
import turtle
import time


class Square:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def drawself(self, turtle):
        # draw a black box at its coordinates, leaving a small gap between cubes
        turtle.goto(self.x - 9, self.y - 9)
        turtle.begin_fill()
        turtle.color(self.color)
        for i in range(4):
            turtle.forward(18)
            turtle.left(90)
        turtle.end_fill()


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = "ON"
        self.color = "darkred"

    def changelocation(self):
        # I haven't programmed it to spawn outside the snake's body yet
        self.x = random.randint(0, 20)*20 - 200
        self.y = random.randint(0, 20)*20 - 200

    def drawself(self, turtle):
        # similar to the Square drawself, but blinks on and off
        if self.state == "ON":
            turtle.goto(self.x - 9, self.y - 9)
            turtle.color(self.color)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(18)
                turtle.left(90)
            turtle.end_fill()

    def changestate(self):
        # controls the blinking
        self.state = "OFF" if self.state == "ON" else "ON"


class Snake:
    def __init__(self):
        self.headposition = [20, 0] # keeps track of where it needs to go next
        self.color = "forestgreen"
        self.body = [Square(-20, 0, self.color), Square(0, 0, self.color), Square(20, 0, self.color)] # body is a list of squares
        self.nextX = 1 # tells the snake which way it's going next
        self.nextY = 0   
        self.crashed = False # I'll use this when I get around to collision detection
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                             self.headposition[1] + 20*self.nextY]
        # prepares the next location to add to the snake

    def moveOneStep(self):
        if Square(self.nextposition[0], self.nextposition[1], self.color) not in self.body:
            # attempt (unsuccessful) at collision detection
            self.body.append(Square(self.nextposition[0], self.nextposition[1], self.color))
            # moves the snake head to the next spot, deleting the tail
            del self.body[0]
            self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
        # resets the head and nextposition
            self.nextposition = [self.headposition[0] + 20*self.nextX,
                                 self.headposition[1] + 20*self.nextY]
        else:
            self.crashed = True # more unsuccessful collision detection

    def moveup(self): # pretty obvious what these do
        self.nextX = 0
        self.nextY = 1

    def moveleft(self):
        self.nextX = -1
        self.nextY = 0

    def moveright(self):
        self.nextX = 1
        self.nextY = 0

    def movedown(self):
        self.nextX = 0
        self.nextY = -1

    def eatFood(self):
        # adds the next spot without deleting the tail, extending the snake by 1
        self.body.append(Square(self.nextposition[0], self.nextposition[1], self.color))
        self.headposition[0], self.headposition[1] = self.body[-1].x, self.body[-1].y
        self.nextposition = [self.headposition[0] + 20*self.nextX,
                             self.headposition[1] + 20*self.nextY]

    def drawself(self, turtle): # draws the whole snake when called
        for segment in self.body:
            segment.drawself(turtle)


class Game:
    def __init__(self):
        # game object has a screen, a turtle, a basic snake and a food
        self.screen = turtle.Screen()
        self.artist = turtle.Turtle()
        self.artist.up()
        self.artist.hideturtle()
        self.snake = Snake()
        self.food = Food(100, 0)
        self.counter = 0 # this will be used later
        self.commandpending = False # as will this 

        self.grid_extent = 400 # this is the max extension of the grid in one direction
                               # the grid size is douple that
        self.box_size = 20     # The box size
        self.grid_shift = self.box_size / 2  # Since the turtle draws the box from its center we need to shift the grid one half

        self.top_left = [
            self.grid_shift-self.grid_extent, # = X
            self.grid_extent+self.grid_shift  # = Y
        ]
        self.bottom_right = [
            self.grid_shift+self.grid_extent, # = X
            self.grid_extent-self.grid_shift  # = Y
        ]

    def nextFrame(self):
        while True: # now here's where it gets fiddly...
            game.screen.listen()
            game.screen.onkey(game.snakedown, "Down")
            game.screen.onkey(game.snakeup, "Up")
            game.screen.onkey(game.snakeleft, "Left")
            game.screen.onkey(game.snakeright, "Right")
            turtle.tracer(0) # follow it so far?
            self.artist.clear()
            if self.counter == 2:
            # only moves to next frame every 5 loops, this was an attempt to get rid of the turning delay
                if (self.snake.nextposition[0], self.snake.nextposition[1]) == (self.food.x, self.food.y):
                    self.snake.eatFood()
                    self.food.changelocation()
                else:
                    self.snake.moveOneStep()
                self.counter = 0
            else:
                self.counter += 1
            self.food.changestate() # makes the food flash 
            self.drawself(self.artist)
            self.food.drawself(self.artist) # show the food and snake
            self.snake.drawself(self.artist)
            turtle.update()
            self.commandpending = False
            time.sleep(0.05) 

    def draw_border(self, turtle):
        turtle.color("black")
        turtle.penup()
        turtle.goto(self.top_left[0], self.top_left[1])
        turtle.pensize(5)
        turtle.pendown()
        for i in range(4):
            turtle.forward(2*self.grid_extent)
            turtle.right(90)
        turtle.penup()

    def drawself(self, turtle):
        self.draw_grid(turtle)
        self.draw_border(turtle)
        turtle.penup()

    def draw_grid(self, turtle):
        # grid lines
        turtle.color("grey")
        turtle.pensize(1)
        for i in xrange(self.top_left[0], self.bottom_right[0], self.box_size):
            turtle.penup()
            turtle.goto(i, self.top_left[0])
            turtle.pendown()
            turtle.right(270)
            turtle.forward(2*self.grid_extent)
            turtle.left(270)
            turtle.penup()
            turtle.goto(self.top_left[0], i)
            turtle.pendown()
            turtle.forward(2*self.grid_extent)
            turtle.penup()
        turtle.penup()
        

    def snakeup(self):
        print("going up") # put this in for debugging purposes
        if not self.commandpending:
        # should allow only one turn each frame; I don't think it's working
            self.snake.moveup()
            self.commandpending = True

    def snakedown(self):
        print("going down")
        if not self.commandpending:
            self.snake.movedown()
            self.commandpending = True

    def snakeleft(self):
        print("going left")
        if not self.commandpending:
            self.snake.moveleft()
            self.commandpending = True

    def snakeright(self):
        print("going right")
        if not self.commandpending:
            self.snake.moveright()
            self.commandpending = True


game = Game()
game.nextFrame()
print("game over!")

game.screen.mainloop()
