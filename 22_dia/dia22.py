import requests
import json
from bs4 import BeautifulSoup

# url = 'https://archive.ics.uci.edu/ml/datasets.php'

# response = requests.get(url)

# content = response.content
# soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.get_text())
# # print(soup.body)
# tables = soup.find_all('table', {'cellpadding': '3'})
# table = tables[0]
# print(table)
# for td in table.find('tr').find_all('td'):
#     print(td.text)

# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
"""
url2 = 'http://www.bu.edu/president/boston-university-facts-stats/'

response2 = requests.get(url2)
contened = response2.content
soup = BeautifulSoup(contened, 'html.parser')
lista = soup.find_all('li', {'class': 'list-item'})
new_dict = {}
for li in lista:
    # print(li.p.text, li.span.text)
    new_dict[li.p.text] = li.span.text

with open("bu.edu.json", "w") as f:
    json.dump(new_dict, f)

"""
# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file


def web_scrap(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table', {'cellpadding': '5', 'border': '1'})
    table = tables[0]
    head_keys = []
    for td in table.find_all('tr'):
        head_keys.append(td)

    print(head_keys)


web_scrap('https://archive.ics.uci.edu/ml/datasets.php')
