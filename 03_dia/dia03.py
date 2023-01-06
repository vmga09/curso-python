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


print('the slope, x-intercept and y-intercept of y = 2x -2')
slope1 = 2
y = 0
x_intercept = (y + 2)/2
x = 0
y_intercept = 2*x - 2
print(x_intercept, y_intercept, slope1)


"""
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

"""


point1 = (2, 2)
point2 = (6, 10)
slope2 = (point2[1]-point1[1])/(point2[0]-point1[0])
euclidean = ((point2[1]-point1[1])**2 + (point2[0]-point1[0])**2)**0.5
print('The slope: ', slope2, 'Distance euclidena: ', euclidean)


"""
Compare the slopes in tasks 8 and 9.

"""


print(slope1 is slope2)


"""
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

"""

super_x = float(input('Ingrese valor de x'))
funcion = super_x**2 + 6*super_x + 9
print('resultado de la funcion y = x^2 + 6x + 9 es :', funcion)

"""
Find the length of 'python' and 'dragon' and make a falsy comparison statement.

"""

print('La comparacion entre largo "python" y "dragon" es: ',
      len('python') is len('dragon'))

"""
Use and operator to check if 'on' is found in both 'python' and 'dragon'

"""

print('La palabra "on" esta contenida en python y dragon?',
      'on' in 'dragon' and 'on' in 'python')


"""
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

"""

print('jargon' in 'I hope this course is not full of jargon')

"""
There is no 'on' in both dragon and python

"""

print(not ('on' in 'python' and 'on' in 'dragon'))


# Find the length of the text python and convert the value to float and convert it to string

print(str(float(len('dragon'))))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

res = input('Ingrese Numero divisible: ')
print(int(res) % 2 == 0)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

print(7 // 3 == int(2.7))


# Check if type of '10' is equal to type of 10

print('Si "10" es igual a 10: ', type('10') == type(10))


# Check if int('9.8') is equal to 10

print(" Verificar que int(9.8) es igual a 10: ", int(9.8) == 10)


# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = float(input('Ingrese horas'))
rate = float(input('Sueldo por hora'))

print('Tu salario es: ', hours*rate)


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = float(input('Ingrese años'))
print('Total de segundos vividos es: ', years*365*24*60*60)


# Write a Python script that displays the following table

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
