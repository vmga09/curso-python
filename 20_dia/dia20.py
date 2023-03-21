import requests

url = 'https://restcountries.com/v3.1/all' # text from a website

response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
name_country =  []
countries = response.json()
# for country in countries:
#     name_country.append({"name": country['name']['common'], "capital": country.capital[0]})
for country in countries:
    try:
        print(country['capital'])
    except KeyError:
        print('No Capital')
# print(countries[0]['capital'][0])
# print(name_country)


