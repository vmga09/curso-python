# Module re

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# print(re.findall('a', txt, re.I))
busqueda = re.search('a', txt, re.I)
print(busqueda)
start, end = busqueda.span()
print(start, end)
print(txt[start:end])  # Substring

match_replace = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replace)

match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)

# Replacing a Substring

texto = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', texto)
print(matches)

# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))  # splitting using \n - end of line symbol

regex_pattern = r'[Aa].ple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[Aa]pple|[Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)

# Escape character(\) in RegEx , One or more times(+)
regex_pattern = r'\d+'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)


# 💻 Exercises: Day 18
# Exercises: Level 1

# What is the most frequent word in the following paragraph?

# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


def most_frequent(text):
    new_arr = []
    # match_replace = re.sub('\.', '', text, re.I).split()
    match_replace = list(set(re.findall(r'\w+', text)))
    print(match_replace)
    for item in match_replace:
        matches = len(re.findall(item, text))
        new_tupla = (matches, item)
        new_arr.append(new_tupla)

    print(new_arr)


most_frequent(paragraph)


# [
#     (6, 'love'),
#     (5, 'you'),
#     (3, 'can'),
#     (2, 'what'),
#     (2, 'teaching'),
#     (2, 'not'),
#     (2, 'else'),
#     (2, 'do'),
#     (2, 'I'),
#     (1, 'which'),
#     (1, 'to'),
#     (1, 'the'),
#     (1, 'something'),
#     (1, 'if'),
#     (1, 'give'),
#     (1, 'develop'),
#     (1, 'capabilities'),
#     (1, 'application'),
#     (1, 'an'),
#     (1, 'all'),
#     (1, 'Python'),
#     (1, 'If')
# ]

# The position of some particles on the horizontal x-axis are - 12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

# points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
# sorted_points = [-4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 - (-4)  # 12

# Exercises: Level 2

# Write a pattern which identifies if a string is a valid python variable

# is_valid_variable('first_name')  # True
# is_valid_variable('first-name')  # False
# is_valid_variable('1first_name')  # False
# is_valid_variable('firstname')  # True

def is_valid_variable(variable):
    regex_pattern = r'^[a-zA-Z]\w*$'
    matches = re.match(regex_pattern, variable)
    print(matches)


is_valid_variable('hola-como')
is_valid_variable('hola_como')
is_valid_variable('1hola_como')

# Exercises: Level 3

# Clean the following text. After cleaning, count three most frequent words in the string.

# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
# print(most_frequent_words(cleaned_text))

# 🎉 CONGRATULATIONS ! 🎉
