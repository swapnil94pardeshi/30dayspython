import requests
from bs4 import BeautifulSoup

'''
url = 'https://archive.ics.uci.edu/datasets'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)
tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)


#Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').


import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

data = {}

facts_stats = soup.find_all('div', class_='facts-stats')
for fact in facts_stats:
    # Using sub-sections to categorize data
    category_header = fact.find_previous('h3')
    if category_header:
        category = category_header.get_text(strip=True)
        data[category] = []
    items = fact.find_all('div', class_='fact')
    for item in items:
        value = item.find('h2').get_text(strip=True)
        description = item.find('p').get_text(strip=True)
        data[category].append({'value': value, 'description': description})



sections = soup.find_all(['h2', 'h4'])
current_category = None
for section in sections:
    if section.name == 'h2':
        current_category = section.get_text(strip=True)
        data[current_category] = []
    elif section.name == 'h4' and current_category:
        value = section.get_text(strip=True)
        next_p = section.find_next_sibling('p')
        if next_p:
            description = next_p.get_text(strip=True)
            data[current_category].append({'value': value, 'description': description})


with open('bu_facts_stats.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('Data scraped and saved to bu_facts_stats.json')


#Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file

import requests
import pandas as pd

# URL of the UCI Machine Learning Repository datasets page
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Fetch the page content
response = requests.get(url)

# Use pandas to read the HTML tables
dfs = pd.read_html(response.content)

# The desired table is usually the first one, but you can check the list if needed
df = dfs[5]

# Convert DataFrame to JSON
data_json = df.to_json(orient='records')

# Write the JSON data to a file
with open('uci_datasets.json', 'w') as json_file:
    json_file.write(data_json)

print('Data scraped and saved to uci_datasets.json')
'''

#Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.

import requests
from bs4 import BeautifulSoup
import json

url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


table = soup.find('table', {'class': 'wikitable'})


presidents = []

rows = table.find_all('tr')[1:]

for row in rows:
    cells = row.find_all(['th', 'td'])
    if len(cells) > 0:
        president = {
            'number': cells[0].get_text(strip=True),
            'name': cells[1].get_text(strip=True),
            'term_start': cells[2].get_text(strip=True),
            'term_end': cells[3].get_text(strip=True),
            'party': cells[4].get_text(strip=True),
            'vice_president': cells[5].get_text(strip=True)
        }
        presidents.append(president)


with open('presidents.json', 'w') as json_file:
    json.dump(presidents, json_file, indent=4)