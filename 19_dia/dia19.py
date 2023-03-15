# read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.

import json
import os
f = open(
    'C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\grado.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
# readline(): read only the first line

f = open('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\grado.txt')
line = f.readline()
print(type(line))
print(line)
f.close()

# readlines(): read all the text line by line and returns a list of lines
f = open('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\grado.txt')
lines = f.readlines()
print(type(lines))  # Return list of lines
print(lines)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\grado.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# Open file with close
with open('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\grado.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# Opening Files write updating
with open('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\grado.txt', 'a') as f:
    f.write('This text has to be appended at the end\n')

# The method below creates a new file, if the file does not exist:
with open('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\new_grado.txt', 'w') as f:
    f.write('This text will be written in a newly created file')

# Deleting file
try:

    os.remove(
        'C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\new2_grado.txt')
except Exception as e:
    print(e)


if os.path.exists('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\new_grado.txt'):
    os.remove(
        'C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\new_grado.txt')
    print('File Removed')
else:
    print('The file does not exist')


# Json file

with open('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\jason_example.json') as js:
    person_json = js.read()
    person_dct = json.loads(person_json)
    print(type(person_dct))
    print(person_dct)
    print(person_dct['name'])

personal = {
    "name": "Victor_Gonzalez",
    "country": "Chile",
    "city": "Santiago",
    "skills": ["JavaScrip", "Angular", "Python"]
}

with open(f'C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\{personal["name"]}.json', 'w', encoding='utf-8') as f:
    json.dump(personal, f, ensure_ascii=False, indent=4)


# 💻 Exercises: Day 19
# Exercises: Level 1

# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words


def read_texto(file):
    with open(f'C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\{file}.txt') as fl:
        texto = fl.read()
        lines = texto.splitlines()
        words = texto.split(" ")
        print(
            f'Para {file.upper()} el número de líneas :{len(lines)} y el número de palabras es: {len(words)}')


speech = ['donald_speech', 'melina_trump_speech',
          'obama_speech', 'michelle_obama_speech']


def count_wl(speech):
    for file in speech:
        read_texto(file)


count_wl(speech)


#     Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

def read_json_file():
    with open('C:\\Users\\13181784\\Documents\\Desarrollo Activos\\curso-python\\19_dia\\countries_data.json', encoding="utf8") as cj:
        countries_data = cj.read()  # formato str
        # tranforma en una lista con json
        countries_json = json.loads(countries_data)
        print(type(countries_json))


read_json_file()


#     # Your output should look like this
#     print(most_spoken_languages(filename='./data/countries_data.json', 10))
#     [(91, 'English'),
#      (45, 'French'),
#      (25, 'Arabic'),
#      (24, 'Spanish'),
#      (9, 'Russian'),
#      (9, 'Portuguese'),
#      (8, 'Dutch'),
#      (7, 'German'),
#      (5, 'Chinese'),
#      (4, 'Swahili'),
#      (4, 'Serbian')]

#     # Your output should look like this
#     print(most_spoken_languages(filename='./data/countries_data.json', 3))
#     [(91, 'English'),
#      (45, 'French'),
#      (25, 'Arabic')]

#     Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

#     # Your output should look like this
#     print(most_populated_countries(filename='./data/countries_data.json', 10))

#     [
#      {'country': 'China', 'population': 1377422166},
#      {'country': 'India', 'population': 1295210000},
#      {'country': 'United States of America', 'population': 323947000},
#      {'country': 'Indonesia', 'population': 258705000},
#      {'country': 'Brazil', 'population': 206135893},
#      {'country': 'Pakistan', 'population': 194125062},
#      {'country': 'Nigeria', 'population': 186988000},
#      {'country': 'Bangladesh', 'population': 161006790},
#      {'country': 'Russian Federation', 'population': 146599183},
#      {'country': 'Japan', 'population': 126960000}
#      ]

#     # Your output should look like this

#     print(most_populated_countries(filename='./data/countries_data.json', 3))
#     [
#      {'country': 'China', 'population': 1377422166},
#      {'country': 'India', 'population': 1295210000},
#      {'country': 'United States of America', 'population': 323947000}
#      ]

#     Exercises: Level 2

#     Extract all incoming email addresses as a list from the email_exchange_big.txt file.
#     Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#      (8, 'be'),
#      (6, 'to'),
#      (6, 'of'),
#      (5, 'and'),
#      (4, 'a'),
#      (4, 'in'),
#      (3, 'that'),
#      (2, 'have'),
#      (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#      (8, 'be'),
#      (6, 'to'),
#      (6, 'of'),
#      (5, 'and')]

#     Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
#     Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
#     Find the 10 most repeated words in the romeo_and_juliet.txt
#     Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript

#     Exercises: Level 3

#     🎉 CONGRATULATIONS ! 🎉
