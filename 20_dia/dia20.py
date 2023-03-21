import requests
import re
import statistics
from mypackage import arithmetics, greet

# url = 'https://restcountries.com/v3.1/all'  # text from a website

# response = requests.get(url)  # opening a network and fetching a data
# # print(response)
# # print(response.status_code) # status code, success:200
# # print(response.headers)     # headers information
# name_country = []
# countries = response.json()
# # for country in countries:
# #     name_country.append({"name": country['name']['common'], "capital": country.capital[0]})
# for country in countries:
#     try:
#         print(country['capital'])
#     except KeyError:
#         print('No Capital')
# print(countries[0]['capital'][0])
# print(name_country)

print(arithmetics.add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9))
print(arithmetics.subtract(9, 2))
print(arithmetics.division(5, 3))
print(arithmetics.multiple(6, 78))
print(arithmetics.power(7, 7))
print(greet.greet_person('VICTOR ', 'GONZALEZ'))


# Exercises: Day 20

#   Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

def read_count(url, num):
    # Patron de expresion regular para eliminar digitos comas , etc
    pattern = r'[0-9.,"\'-?:!;\n\r]'
    # Obtener archivo de texto desde la API
    response = requests.get(url)
    # Separa el texto en un arreglo de plabras
    new_text = re.sub(pattern, '', response.text).split(' ')
    # cuentas las ocurrencias de cada palabra y genera un diccionario
    ocurrencias = dict((i, new_text.count(i)) for i in new_text)
    # Ordena la lista en forma decendente
    sort_ocurrencias = sorted(
        ocurrencias.items(), key=lambda x: x[1], reverse=True)
    print(sort_ocurrencias[1:num+1])


# read_count('http://www.gutenberg.org/files/1112/1112.txt', 10)

#    Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find:


def stat_cats_api():
    url = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(url)
    cats = response.json()
    weight = []
    lifespan = []
    for cat in cats:
        weight.append(int(cat['weight']['metric'].split(' ')[-1]))
        lifespan.append(int(cat['life_span'].split(' ')[-1]))
    # print(int(cats[0]['weight']['metric'].split(' ')[-1]))
    print(f'''    El min weight {min(weight)}
    El max weight {max(weight)}
    El promedio {round(sum(weight)/len(weight),2)}
    La Mediana weight {weight[int((len(weight)+1)/2)]}
    La desviacion standar es: {statistics.pstdev(weight)}
     El min vida {min(lifespan)}
    El max vida {max(lifespan)}
    El promedio vida {round(sum(lifespan)/len(lifespan),2)}
    La Mediana vida {lifespan[int((len(lifespan)+1)/2)]}
    La desviacion standar de vida es: {statistics.pstdev(lifespan)} ''')


stat_cats_api()


#         the min, max, mean, median, standard deviation of cats' weight in metric units.
#         the min, max, mean, median, standard deviation of cats' lifespan in years.
#         Create a frequency table of country and breed of cats
#     Read the countries API and find
#       the 10 largest countries
#        the 10 most spoken languages
#         the total number of languages in the countries API
#     UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https: // archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

# 🎉 CONGRATULATIONS ! 🎉
