"""
Declare your age as integer variable
"""

my_age = 45

print(my_age)

"""
Declare your height as a float variable

"""

my_height = 86.5

print(my_height)

"""
Declare a variable that store a complex number

"""

my_complex_number = 1 + 2j

print(my_complex_number)

"""
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

"""


def calculate_area():
    base = float(input('Enter base:'))
    height = float(input('Enter height:'))
    area = 0.5*(height*base)
    return print(area)


calculate_area()


"""
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

"""


def calculate_perimeter():
    a = float(input('Enter a:'))
    b = float(input('Enter b:'))
    c = float(input('Enter c:'))
    perimeter = a + b + c
    return print(perimeter)


calculate_perimeter()


"""
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

"""


def calculate_rectangle():
    length = float(input('Enter length:'))
    width = float(input('Enter width:'))
    area = length * width
    perimeter = 2 * (length + width)
    return print(area), print(perimeter)


calculate_rectangle()


"""

Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

"""


def calculate_circle():
    pi = 3.14
    r = float(input('Enter radius:'))
    area = pi * r*r
    circumference = 2 * pi * r
    return print(area), print(circumference)


calculate_circle()

"""
Calculate the slope, x-intercept and y-intercept of y = 2x -2

"""


def calculate_slope():
    print('the slope, x-intercept and y-intercept of y = 2x -2')
    slope = 2
    y = 0
    x_intercept = (y + 2)/2
    x = 0
    y_intercept = 2*x - 2
    return print(x_intercept, y_intercept, slope)


calculate_slope()


"""
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

"""


def calculate_slope_euclidean():
    point1 = (2, 2)
    point2 = (6, 10)
    slope = (point2[1]-point1[1])/(point2[0]-point1[0])
    euclidean = ((point2[1]-point1[1])**2 + (point2[0]-point1[0])**2)**0.5
    return print('The slope: ', slope, 'Distance euclidena: ', euclidean)


calculate_slope_euclidean()
