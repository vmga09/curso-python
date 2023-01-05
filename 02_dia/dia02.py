

# Variables
first_name = "Victor"  # Variable string
last_name = "Gonzalez"
country = 'chile'
city = 'Santiago'
age = 45  # Variable integer
is_married = True  # Variable boolean
skills = ['nodejs', 'javascript', 'html',
          'python', 'bash']  # Variable array of skills
personal_info = {
    'first_name': first_name,
    'last_name': last_name,
    'country': country,
    'city': city,
    'age': age
}  # Variable object

# Print variables
print('First name: ' + first_name)
print('Last name: ', last_name)
print(len(first_name))
print('Age: ', age)
print('Personal info: ', personal_info)


# Functions input
def get_first_name():
    new_first_name = input('What is your first name: ')
    new_age = input('What is your age: ')
    print('Hello: ', new_first_name, 'of Age: ', new_age)


get_first_name()

# Definir multiples variables
mi_nombre, mi_apellido, mi_edad, estoy_casado = 'Victor', 'Gonzalez', 45, True
print(mi_nombre)
print(mi_apellido)
print(mi_nombre, mi_apellido, mi_edad, estoy_casado)


"""
Convertir tipo de datos

"""
# De entero a float
num_int = 10
print(type(num_int))
num_float = float(num_int)
print('num float:', num_float)
print(type(num_float))

# De float a int
pi = 3.1416
print(int(pi))

# de int to str
new_num = 100
num_str = str(new_num)

print(new_num, num_str)

# str to int or float
# num_str = '10.34'
# print('num_int:', int(num_str))
# print('num_float:', float(num_str))
num_str = '10.6'
# Al tener un puntio debe pasar a float
print('num_int', int(float(num_str)))
print('num_float', float(num_str))  # 10.6


# string to list

new_name = 'Victor'
str_to_list = list(new_name)
print(str_to_list)


"""
Declare 5 as num_one and 4 as num_two

    Add num_one and num_two and assign the value to a variable total
    Subtract num_two from num_one and assign the value to a variable diff
    Multiply num_two and num_one and assign the value to a variable product
    Divide num_one by num_two and assign the value to a variable division
    Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    Calculate num_one to the power of num_two and assign the value to a variable exp
    Find floor division of num_one by num_two and assign the value to a variable floor_division

"""


def operation():
    num_one, num_two = 5, 4
    total = num_one + num_two
    diff = num_two - num_one
    product = num_one*num_two
    division = num_one / num_two
    remainder = num_two % num_one
    exp = num_one ** num_two
    floor_division = num_one // num_two
    print(total, diff, product, division, remainder, exp, floor_division)


operation()


"""
The radius of a circle is 30 meters.

    Calculate the area of a circle and assign the value to a variable name of area_of_circle
    Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    Take radius as user input and calculate the area.


"""


# Area ded un circulo
area_circulo = 3.14*(30**2)
print(area_circulo)

# Circunferencia de un circulo
circum_of_circle = 3.14*30*2
print(circum_of_circle)

# Calculo del area de un circulo


def areaCircle(rad):
    return print(3.14*(rad**2))


areaCircle(float(input('Ingrese radio:')))


"""
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

"""


def get_user_input():
    name = input('Ingrese name:' + '\n')
    last_name = input('Ingrese last name:' + '\n')
    country = input('Ingrese country:' + '\n')
    age = input('Ingrese age:' + '\n')
    return print(name, last_name, country, age)


get_user_input()


"""
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

"""


print(help('keywords'))
