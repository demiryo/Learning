"""
general quadratic equation is: f(x)/y = ax^2+bx+c=0
ask user to imput a,b,c. then it will caltulate the following
    - detrminant b^2-4ac
    -result type : rational, decmal, compelx
    - solution/ y solution
    -plot curve
"""

def askuserforabc():
    # ask user for a b c
    print("general quadratic equation is: f(x)/y = ax^2+bx+c=0")
    a = int(raw_input(" input a = "))
    b = int(raw_input(" input b = "))
    c = int(raw_input(" input c = "))

    return (a, b, c)

def ditrminat(a, b, c):
    return b**2-(4*a*c)

def type_ofporabula(a):
    if a > 0:
        # if a is >0 then the parabola opens up
        return "parabola opens up"
    elif a < 0:
        return "parabola opens down"

    # the remaining case is that a = 0, which make a strait line
    return "a strait line!"

if __name__ == "__main__":
    a, b, c = askuserforabc()
    print("a={0}, b={1}, c={2}".format(a, b, c))
    dit= ditrminat(a, b, c)
    print("determinant={}".format(dit))
    type = type_ofporabula(a)
    print (type)

