############## Conditional #########################

# 💻 Exercises: Day 9
# Exercises: Level 1
# 1.  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#     ```sh
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.
#     ```

age = input('Enter your age:\t')
if int(age) > 17:
    print('You are old enough to learn to drive.')
else:
    rest = 18 - int(age)
    print('You need {} more years to learn to drive.'.format(rest))


# 2.  Compare the values of my_age and your_age using if … else. Who is o10lder (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#     ```sh
#     Enter your age: 30
#     You are 5 years older than me.
#     ```

new_age = input('Enter your age:\t')
my_age = 45
if int(new_age) > my_age:
    diff = int(new_age) - my_age
    print('You are {} years older than me.'.format(diff))
else:
    rest = my_age - int(new_age)
    print('You need {} more years to me.'.format(rest))

# 3.  Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# ```sh
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# ```

number_one = input('Enter number one\t')
number_two = input('Enter number two\t')
if int(number_one) > int(number_two):
    print('{} is greater than {}'.format(number_one, number_two))
elif int(number_one) < int(number_two):
    print('{} is greater than {}'.format(number_two, number_one))
else:
    print('{} is equal to {}'.format(number_two, number_one))


#     ### Exercises: Level 2
#    1. Write a code which gives grade to students according to theirs scores:

#         ```sh
#         80-100, A
#         70-89, B
#         60-69, C
#         50-59, D
#         0-49, F
#         ```

studentname = input('Enter name of student')
score = input('Enter score of student')
if int(score) < 50:
    print('The score for {} is "F"'.format(studentname))
elif int(score) > 49 and int(score) < 60:
    print('The score for {} is "D"'.format(studentname))
elif int(score) > 59 and int(score) < 70:
    print('The score for {} is "C"'.format(studentname))
elif int(score) > 69 and int(score) < 80:
    print('The score for {} is "B"'.format(studentname))
elif int(score) > 79 and int(score) < 101:
    print('The score for {} is "A"'.format(studentname))
else:
    print('Enter again score, the number is not correct ')
# 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer

autumn = ['September', 'October', 'November']
winter = ['December', 'Jaunary', 'Febraury']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

month = input('Enter month: ')
if str(month) in autumn:
    print('El mes: {} correspnde a Autumn'.format(str(month)))
elif str(month) in winter:
    print('El mes: {} correspnde a Winter'.format(str(month)))
elif str(month) in spring:
    print('El mes: {} correspnde a Spring'.format(str(month)))
elif str(month) in summer:
    print('El mes: {} correspnde a Summer'.format(str(month)))
else:
    print('Dato ingresado no válido')
# 2.  The following list contains some fruits:
#     ```sh
#     fruits = ['banana', 'orange', 'mango', 'lemon']
#     ```
#     If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = input('Enter fruit:\t')
if str(fruta) in fruits:
    print(' La fruta {} ya esta registrada'.format(fruta))
else:
    fruits.append(str(fruta))
    print(fruits)

#     ### Exercises: Level 3
#    1. Here we have a person dictionary. Feel free to modify it!


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

frontEnd = {'JavaScript', 'React'}
backEnd = {'Node', 'MongoDB', 'Python'}
fullStack = {'React', 'Node', 'MongoDB'}
all_skill = set(person['skills'])
print(all_skill)

if 'skills' in person.keys():
    new_skills = person['skills'][int(len(person['skills'])/2)]
    print('Tiene skill {}'.format(new_skills))
    if 'Python' in person['skills']:
        print('Tiene skills {}'.format('Python'))
    else:
        print('No tiene python')
    if (frontEnd.symmetric_difference(all_skill)) == set():
        print('He is a front end developer')
    elif (backEnd.symmetric_difference(all_skill)) == set():
        print('He is a backend developer')
    elif (fullStack.symmetric_difference(all_skill)) == set():
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print('No skills')

if person['is_marred'] == True and person['country'] == 'Finland':
    print('{} {} lives in {}. He is married'.format(
        str(person['first_name']), str(person['last_name']), str(person['country'])))

#      * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#      * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#      * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#      * If the person is married and if he lives in Finland, print the information in the following format:
# ```py
#     Asabeneh Yetayeh lives in Finland. He is married.
# ```

# 🎉 CONGRATULATIONS ! 🎉
