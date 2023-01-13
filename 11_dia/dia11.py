############## FUNCTION ################################
# 💻 Exercises: Day 11
# Exercises: Level 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(num1, num2):
    sum = num1 + num2
    return print(sum)


#add_two_numbers(4, 5)

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.


def area_of_circle(radio):
    area = 3.14 * radio * radio
    return print('EL AREA ES: {}'.format(area))


#area_of_circle(9)


def ver_num(args):
    if type(args) is int or type(args) is float:
        print('SI')


#ver_num(6.3)
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if type(num) is int or type(num) is float:
            total += num

    return print(total)


#add_all_nums(4, 5, 6, 7, 8.9, 'k')

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def celsius_to_fahrenheit(temp):
    if type(temp) is str:
        print('Ingrese numero válido')
    else:
        temp_f = (temp*9)/5 + 32
        return print('The celcius {} to fahrenheit {}'.format(temp, temp_f))


#celsius_to_fahrenheit(78.9)
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.


def season(month):
    autumn = ['September', 'October', 'November']
    winter = ['December', 'Jaunary', 'Febraury']
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']

    if str(month) in autumn:
        return print('El mes: {} correspnde a Autumn'.format(str(month)))
    elif str(month) in winter:
        return print('El mes: {} correspnde a Winter'.format(str(month)))
    elif str(month) in spring:
        return print('El mes: {} correspnde a Spring'.format(str(month)))
    elif str(month) in summer:
        return print('El mes: {} correspnde a Summer'.format(str(month)))
    else:
        return print('Dato ingresado no válido')


#season(input('Enter month: '))

# Write a function called calculate_slope which return the slope of a linear equation


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return print(' No es una ecuacion cuadrática')
    else:
        raiz = (b*b - 4*a*c)/(2*a)
        print(str(raiz))
        if raiz < 0:
            return print('No tiene solución')
        elif raiz == 0:
            x1 = -b/(2*a)
            return print(' La ecuación pasa por unico punto: {}'.format(str(x1)))
        else:
            x1 = (-b + raiz)/(2*a)
            x2 = (-b - raiz)/(2*a)
            return print(' La ecuación pasa por los puntos: {} y {}'.format(str(x1), str(x2)))


#solve_quadratic_eqn(1, 6, 8)

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


def print_list(list):
    for item in list:
        print(item)


#print_list([3, 4, 56, 6, 7])
# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array(use loops).


# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]

def reverse_list(list):
    new_arr = []
    for i in range(len(list) - 1, -1, -1):
        new_arr.append(list[i])

    return print(new_arr)


#reverse_list(["A", "B", "C"])

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(array):
    new_arr = []
    for item in array:
        new_arr.append(str(item).capitalize())

    print(new_arr)


#capitalize_list_items(['qwqw', 'erwer', 4])
# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']


def add_item(list, item):
    list.append(item)
    return list


#print(add_item(food_staff, 'Yogurt'))

# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# print(add_item(food_staff, 'Meat'))
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))[2, 3, 7, 9, 5]


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]

numbers = [2, 3, 7, 9]


def remove_item(list, item):
    if item in list:
        list.remove(item)
        return list
    else:
        print('Item not found')
        return list


#print(remove_item(numbers, 4))


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.


# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10))  # 55
# print(sum_all_numbers(100))  # 5050

def sum_of_numbers(num):
    sum = 0
    for y in range(num + 1):
        sum += y

    return sum


#print(sum_of_numbers(100))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.


def sum_odd(num):
    odd = 0
    for i in range(num+1):

        if i % 2 != 0:
            odd += i

    print('the sum of all odds is {}'.format(
        str(odd)))


#sum_odd(15)


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.


def sum_even(num):
    even = 0
    for i in range(num+1):

        if i % 2 == 0:
            even += i

    print('The sum of all evens is {}.'.format(
        str(even)))


#sum_even(15)


# Exercises: Level 2

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

# print(evens_and_odds(100))
# # The number of odds are 50.
# # The number of evens are 51.

def sum_odd_even(num):
    even = 0
    odd = 0
    for i in range(num+1):

        if i % 2 == 0:
            even += i
        else:
            odd += i

    print('The sum of all evens is {}. And the sum of all odds is {}'.format(
        str(even), str(odd)))


#sum_odd_even(15)

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


def fact_of_numbers(num):
    fact = 1
    for y in range(1, num + 1, 1):
        fact *= y

    return fact


#print(fact_of_numbers(10))


# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(arg):
    if arg == ' ' or arg == '':
        print('This is empty')
    else:
        print(arg)


#is_empty(' ')
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std(standard deviation).

arreglo = [1,2,3,4,5,6,7,8,9,10]
def calculate_mean(arr):
    sum = 0
    for m in arr:
        sum += m
    avg = sum / len(arr)
    return avg

print(calculate_mean(arreglo))

def calculate_median(arr):
    sorted_data = sorted(arr)
    data_len = len(sorted_data)
    middle = (data_len -1) // 2
    if middle %2:
        return sorted_data[middle]
    else:
        return (sorted_data[middle] + sorted_data[middle+1]) / 2

print(calculate_median(arreglo))


def calculate_mode(arr):
    y = {}
    for a in arr:
        if not a in y:
            y[a] = 1
        else:
            y[a] += 1
    return [ g for g , l in y.items() if l ==max(y.values()) ]


print(calculate_mode([34,23,56,43,56,2,378,54,23,34,12,21,23,45,55]))


def calculate_range(arr):
    sort_arr = sorted(arr)
    range = sort_arr[len(sort_arr)-1] - sort_arr[0]
    return range

print(calculate_range([34,23,56,43,56,2,378,54,23,34,12,21,23,45,55]))


def calculate_variance(arr):
    avg = calculate_mean(arr)
    sum = 0
    for i in arr:
        acum = (i - avg)**2
        sum += acum
    variance = sum/len(arr)
    return variance


def calculate_stdev(arr):
    s = calculate_variance(arr)
    std = s **0.5
    return std



print(calculate_variance([4,8,6,5,3,2,8,9,2,5]))
print(calculate_stdev([4,8,6,5,3,2,8,9,2,5]))





# Exercises: Level 3

# Write a function called is_prime, which checks if a number is prime.
# Write a functions which checks if all items are unique in the list.
# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.

# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

# 🎉 CONGRATULATIONS ! 🎉
