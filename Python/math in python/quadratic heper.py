"""
general quadratic equation is: f(x)/y = ax^2+bx+c=0
ask user to imput a,b,c. then it will caltulate the following
    - detrminant b^2-4ac
    -result type : rational, decmal, compelx
    - solution/ y solution
    -plot curve
"""
import math

#required for plotting
import numpy as np
import pylab

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

def vertex(a,b,c):
    x=-b/(2*a)
    y=(a*x**2)+(b*x)+c
    print ("vertex = ({} , {})".format(x,y))

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
    print vertex(a,b,c)

    plot_quadretic(a, b, c)



############################################
#
#    Plotting code
#

def plot_simple_curve():
    #N = 10
    #X = np.matrix(range(N)).T + 1
    X = np.arange(-5.0, 2.0, 0.01)

    #Y = 2 * X + 1
    # Y = X ** 2 + 2X + 2
    Y = np.square(X) + 2 * X + 2

    pylab.grid()
    pylab.axes().set_aspect(1)

    pylab.plot(X, Y, 'k-')
    #pylab.contour()
    pylab.show()

def quadretic_vertix(a, b, c):
    vertix_x = - b / ( 2 * a )
    vertix_y = (a * vertix_x ** 2) + (b * vertix_x) + c
    return (vertix_x, vertix_y)

def quadretic_range(vertix_x, vertix_y, range_diff, is_concave):
    range_x_min = vertix_x - range_diff
    range_x_max = vertix_x + range_diff
    range_y_min = vertix_y - range_diff + ((range_diff / 2) if is_concave else (- range_diff / 2))
    range_y_max = vertix_y + range_diff + ((range_diff / 2) if is_concave else (- range_diff / 2))
    return (range_x_min, range_x_max, range_y_min, range_y_max)

def plot_setup_grid(range_x_min, range_x_max, range_y_min, range_y_max):
    pylab.grid(True, which='both')
    #pylab.minorticks_on()
    pylab.xticks(np.arange(range_x_min, range_x_max, step=1.0))
    pylab.yticks(np.arange(range_y_min, range_y_max, step=1.0))
    pylab.axis([range_x_min, range_x_max, range_y_min, range_y_max])
    pylab.axes().set_aspect('equal')

def plot_quadretic(a, b, c):
    vertix_x, vertix_y = quadretic_vertix(a,b,c)
    range_x_min, range_x_max, range_y_min, range_y_max = quadretic_range(vertix_x, vertix_y, range_diff = 10, is_concave = (a > 0))

    # calculate X, Y points
    X = np.arange(range_x_min, range_x_max, 0.01 )
    Y =  a * np.square(X) + b * X + c

    plot_setup_grid(range_x_min, range_x_max, range_y_min, range_y_max)
    pylab.title("Y = {}X^2 {:+}X {:+}".format(a, b, c))

    # Actual plotting code
    pylab.plot(X, Y, 'k-')
    pylab.plot(vertix_x, vertix_y, 'ro')
    pylab.annotate(
        "Vertix = {{{}, {}}}".format(vertix_x, vertix_y),
        xy=(vertix_x, vertix_y), xytext=(-20, 20),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
    pylab.show()

#
############################################
if __name__ == "__main__":
    a, b, c = askuserforabc()
    test_ABC(a, b, c)

    #test_ABC(1, 2, 3) #

    #test_ABC(1, 2, 1) # one rational solution

    #test_ABC(1, 1, 1) # Imaginary

