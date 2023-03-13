# #  Ejemplo

# try:
#     print(10 + '5')
# except:
#     print('Something went wrong')


# try:
#     name = input('Enter your name:')
#     year_born = input('Year you were born:')
#     age = 2019 - year_born
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occured')
# except ValueError:
#     print('Value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')


# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# # else:
# #     print('I usually run with the try block')
# # finally:
# #     print('I alway run.')


# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - (year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as error:
#     print(error)

# print('Enter your')


# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e


# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst))  # 15


# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
# print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
# numbers = [1, 2, 3, 4, 5, 6, 7]
# one, *middle, new_last, last = numbers
# print(one, middle, new_last, last)  # 1 [2, 3, 4, 5, 6] 7
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'


dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
# Asabeneh lives in Finland, Helsinki. He is 250 years old.
print(unpacking_person_info(**dct))

for index, item in enumerate([20, 30, 40]):
    print(index, item)


# Exercises: Day 17

# names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

# 🎉 CONGRATULATIONS ! 🎉

names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']


*nordic_countries, es, ru = names

print(nordic_countries, es, ru)
