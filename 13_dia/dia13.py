# 💻 Exercises: Day 13

# Filter only negative and zero in the list using list comprehension

# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
new_numbers = [i for i in numbers if i < 0]
print(new_numbers)

# Flatten the following list of lists of lists to a one dimensional list:

#     list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

#     output
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
new_list = [x for sub in list_of_lists for sub2 in sub for x in sub2]
# flattened_list = [i for row in list_of_lists for i in row]
# new_flattened_list = [i for row in flattened_list for i in row]
print(new_list)


#     Using list comprehension create the following list of tuples:

#     [(0, 1, 0, 0, 0, 0, 0),
#      (1, 1, 1, 1, 1, 1, 1),
#      (2, 1, 2, 4, 8, 16, 32),
#      (3, 1, 3, 9, 27, 81, 243),
#      (4, 1, 4, 16, 64, 256, 1024),
#      (5, 1, 5, 25, 125, 625, 3125),
#      (6, 1, 6, 36, 216, 1296, 7776),
#      (7, 1, 7, 49, 343, 2401, 16807),
#      (8, 1, 8, 64, 512, 4096, 32768),
#      (9, 1, 9, 81, 729, 6561, 59049),
#      (10, 1, 10, 100, 1000, 10000, 100000)]

tuples_rules = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuples_rules)


#     Flatten the following list to a new list:

#     countries = [[('Finland', 'Helsinki')], [
#         ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#     output:
#     [['FINLAND', 'FIN', 'HELSINKI'], [
#         'SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_countries = [[sub2[0].upper(), sub2[0].upper()[0:3], sub2[1].upper()]
                 for sub in countries for sub2 in sub]

print(new_countries)
#     Change the following list to a list of dictionaries:

#     countries = [[('Finland', 'Helsinki')], [
#         ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#     output:
#     [{'country': 'FINLAND', 'city': 'HELSINKI'},
#      {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#      {'country': 'NORWAY', 'city': 'OSLO'}]

new_countries_dic = [{'country': sub2[0].upper(), 'city': sub2[1].upper()}
                     for sub in countries for sub2 in sub]
print(new_countries_dic)

#     Change the following list of lists to a list of concatenated strings:

#     names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
#              [('Donald', 'Trump')], [('Bill', 'Gates')]]
#     output
#     ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_names = [sub2[0] + ' ' + sub2[1] for sub in names for sub2 in sub]
print(new_names)
#     Write a lambda function which can solve a slope or y-intercept of linear functions.


def slope(y1, y2, x1, x2): return (y2 - y1)/(x2-x1)


def y_intercept(x1, y1, x2, y2): return y1 - slope(x1, y1, x2, y2) * x1


print(slope(5, 4, 3, 1))
print(y_intercept(5, 4, 3, 1))
# 🎉 CONGRATULATIONS ! 🎉
