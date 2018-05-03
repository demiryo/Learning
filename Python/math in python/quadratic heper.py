"""
general quadratic equation is: f(x)/y = ax^2+bx+c=0
ask user to imput a,b,c. then it will caltulate the following
    - detrminant b^2-4ac
    -result type : rational, decmal, compelx
    - solution/ y solution
    -plot curve
"""
import math


def askuserforabc():
    # ask user for a b c
    print("general quadratic equation is: f(x)/y = ax^2+bx+c=0")
    valid = False
    while(not valid):
        a = int(raw_input(" input a = "))
        b = int(raw_input(" input b = "))
        c = int(raw_input(" input c = "))
        if a != 0:
            valid = True
        else:
            print "a can't be zero, try again!"

    return (a, b, c)

def ditrminat(a, b, c):
    return b**2-(4*a*c)

def solve(a, b, c):
    dit = ditrminat(a,b,c)
    if dit<0:
        r = ( -b ) / (2 * a)
        i = ( math.sqrt(-dit) ) / (2 * a)
        return "complex solution r={} i=+/-{}".format(r,i)
    elif dit==0:
        s = ( -b ) / (2 * a)
        return ("Only one solution {0}".format(s))

    # General case, 2 real roots
    s1 = (-b - math.sqrt(dit)) / (2 * a)
    s2 = (-b + math.sqrt(dit)) / (2 * a)
    return ("solutions are {0} and {1}".format(s1,s2))


def type_ofporabula(a):
    if a > 0:
        # if a is >0 then the parabola opens up
        return "parabola opens up"
    elif a < 0:
        return "parabola opens down"

    # the remaining case is that a = 0, which make a strait line
    return "a strait line!"

def solution_type(dit):
    if dit<0:
        return"complex solution (imaginary number)"
    elif dit==0:
        return"one rational solution"
    dit_sqrt= math.sqrt(dit)
    if dit_sqrt.is_integer():
        return"two rational solutions"
    return "two real number solutions"

def test_ABC(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))
    dit= ditrminat(a, b, c)
    print("determinant={}".format(dit))
    type = type_ofporabula(a)
    print (type)
    s_type = solution_type(dit)
    print(s_type)
    s = solve(a,b,c)
    print(s)
if __name__ == "__main__":
    a, b, c = askuserforabc()
    test_ABC(a, b, c)

    #test_ABC(1, 2, 3) #

    #test_ABC(1, 2, 1) # one rational solution

    #test_ABC(1, 1, 1) # Imaginary

