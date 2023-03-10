# 💻 Exercises: Day 14

from functools import reduce
import paisesm 

paises = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Exercises: Level 1

# Explain the difference between map, filter, and reduce.
# Explain the difference between higher order function, closure and decorator
# Define a call function before map, filter or reduce, see examples.
# Use for loop to print each country in the countries list.


def print_countries(countries):
    for country in countries:
        print(country)


# Use for to print each name in the names list.
def print_names(names):
    for name in names:
        print(name)
# Use for to print each number in the numbers list.


def print_numbers(numbers):
    for number in numbers:
        print(number)


print_countries(paises)
print_names(names)
print_numbers(numbers)

# Exercises: Level 2

# Use map to create a new list by changing each country to uppercase in the countries list


def uppercase_countries(country):
    return country.upper()


new_contries = list(map(uppercase_countries, paises))
print(new_contries)

new_contries = list(map(lambda x: x.upper(), paises))
print(new_contries)
# Use map to create a new list by changing each number to its square in the numbers list
sqr_numbers = list(map(lambda x: x **2,numbers))
print(sqr_numbers)
# Use map to change each name to uppercase in the names list
uper_names = list(map(lambda x: x.upper(), names))
print(uper_names)
# Use filter to filter out countries containing 'land'.
def find_land(country):
    if 'land' in country:
        return True
    return False


print(list(filter(find_land,paises)))

# Use filter to filter out countries having exactly six characters.

def six_letter(country):
    if len(country) == 6:
        return True
    return False

print(list(filter(six_letter,paises)))  
# Use filter to filter out countries containing six letters and more in the country list.
def six_letterm(country):
    if len(country) >= 6:
        return True
    return False

print(list(filter(six_letterm,paises))) 

# Use filter to filter out countries starting with an 'E'

def init_E(country):
    if country[0] == 'E':
        return True
    return False

print(list(filter(init_E,paises))) 
# Chain two or more list iterators(eg. arr.map(callback).filter(callback).reduce(callback))
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# Use reduce to sum all the numbers in the numbers list.
def _sum_numbers(x,y):
    return x +y

suma = reduce(_sum_numbers,numbers)

print(str(suma))
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

def _concatenate_countries(x,y):
    return x +' '+ y

print(reduce(_concatenate_countries,paises))
# Declare a function called categorize_countries that returns a list of countries with some common pattern(you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
print(list(filter(find_land,paises)))
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

print(paisesm.countries)

keys = []
keys = [i[0] for i in paisesm.countries if i[0] not in keys]
keys_uniq = list(set(keys))

print(keys)
print(keys_uniq)
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

# Exercises: Level 3

# Use the countries_data.py(https: // github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#     Sort countries by name, by capital, by population
#     Sort out the ten most spoken languages by location.
#     Sort out the ten most populated countries.
