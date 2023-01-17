# 💻 Exercises: Day 12
# Exercises: Level 1

#    Writ a function which generates a six digit/character random_user_id.

#      print(random_user_id());
#       '1ee33d'

import string
from random import random, randint
import math


def random_user_id(arg):
    result = ''
    main_string = string.ascii_letters + string.digits
    for i in range(arg):
        newvar = randint(0, len(main_string)-1)
        result += main_string[newvar]

    return print(result)


random_user_id(10)


#     Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# print(user_id_gen_by_user())  # user input: 5 5
# # output:
# # kcsy2
# # SMFYb
# # bWmeq
# # ZXOYh
# # 2Rgxf

def random_users():
    n_user = input('Ingrese numero de users ')
    n_campos = input('Ingrese largo caracteres ')

    main_string = string.ascii_letters + string.digits
    for c in range(int(n_user)):
        result = ''
        for i in range(int(n_campos)):
            newvar = randint(0, len(main_string)-1)
            result += main_string[newvar]

        print(result)


# random_users()
# print(user_id_gen_by_user())  # 16 5
# # 1GCSgPLMaBAVQZ26
# # YD7eFwNQKNs7qXaT
# # ycArC5yrRupyG00S
# # UbGxOFI7UXSWAyKN
# # dIV0SSUTgAdKwStr

#    Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form


def random_rgb():
    rgb = []
    for i in range(3):
        rgb.append(randint(0, 255))

    newrgb = 'rgb'+str(tuple(rgb))

    return newrgb


# print(random_rgb())
# Exercises: Level 2

#     Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after  # . Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
#                                                                                                      Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
#                                                                                                      Write a function generate_colors which can generate any number of hexa or rgb colors.


#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
#         generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
#         generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(arg1, arg2):
    resultrgb = []
    resulthexa = []

    for color in range(arg2):
        rgb = []
        rgbh = ''
        for i in range(3):
            rgb.append(randint(0, 255))
            rgbh += hex(randint(0, 255))[2:]
        resultrgb.append('rgb'+str(tuple(rgb)))
        resulthexa.append('#'+rgbh)

    if arg1 == 'hexa':
        return resulthexa
    elif arg1 == 'rgb':
        return resultrgb
    else:
        return 'Primer argumento {} no es válido'.format(arg1)


print(generate_colors('hexa', 20))


#         Exercises: Level 3

#         Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(lista):

    largo = len(lista)
    largo2 = len(lista)
    print(largo)
    newlist = []
    for i in range(0, largo):
        a = randint(0, largo2 - 1)
        print(a)
        newlist.append(lista[a])
        lista.remove(lista[a])
        largo2 -= 1
    print(newlist, str(largo), str(len(newlist)))


shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])


#         Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def random_number():
    lista = []
    while len(lista) < 7:
        item = randint(0, 9)
        if item not in lista:
            lista.append(item)

    return lista


print(random_number())


#         🎉 CONGRATULATIONS ! 🎉
