from turtle import*

#variables

def get_input_or_default(input_message, defalt_value ):
    """
    this function will take an input message and a default value 
    and will ask the user to enter the value or else use the defalt 
    """
    input_value = input(input_message).strip()
    if input_value == "":
        return defalt_value
    return input_value

print(
    """
press enter right away for the default setting

              1
              1
              V
    """
    )

car_length = int(get_input_or_default("please input the length(default 100): "
                                      , 100))

car_width = int(get_input_or_default("please input the width"
                                     "(default 50, recomend half of length): "
                                     , 50))
                

                
def turtle_default():
    # this is the default turtle state
    color("red")
    width(10)
    

def car_body():
    # this will be the body of the pickup truck

    forward(car_length*3)
    left(90)
    forward(car_width)
    left(90)
    forward(car_length)
    right(90)
    forward(car_width/2)
    width(3.5)
    forward(car_width/4)
    width(10)
    forward(car_width/4)
    left(90)
    forward(car_width/2)
    penup()
    left(90)
    forward(car_width/4)
    pendown()
    width(3.5)
    color("grey")
    forward(car_width/4)
    left(90)
    forward(car_width/2)            
    left(90)
    forward(car_width/4)
    width(3.5)
    left(90)
    forward(car_width/2)
    right(90)
    penup()
    forward(car_width/4)
    turtle_default()
    left(90)
    pendown()
    forward(car_width/2)
    left(90)
    forward(car_width)
    right(90)
    forward(car_length + car_width)
    left(90)
    forward(car_width)
    left(90)
    forward(car_length)

def car_wheel():
    # this will make the car wheels
    
    color("black")
    width(4.5)
    circle(-car_width/3)
    turtle_default()
    forward(car_length)
    color("black")
    width(4.5)
    circle(-car_width/3)
    turtle_default()
    
def make_car():
    # this will actually draw everything, finishing the pickup truck
    turtle_default()    
    car_body()
    car_wheel()

make_car()
    
exitonclick()
                
