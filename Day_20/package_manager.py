'''import requests # importing the request module

url = 'https://www.omdbapi.com/?i=tt3896198&apikey=a1b5c538' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page



import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries




#Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

import requests
import re
from collections import Counter
romeo_and_juliet = 'https://raw.githubusercontent.com/swapnil94pardeshi/mix/main/romeo.txt'
response=requests.get(romeo_and_juliet)
text=response.text
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)
words = text.split()

stopwords = set([
    'the', 'and', 'of', 'to', 'i', 'a', 'in', 'that', 'is', 'was', 'he', 'you', 'it',
    'his', 'with', 'for', 'as', 'had', 'her', 'on', 'at', 'by', 'which', 'have', 'be',
    'this', 'not', 'are', 'but', 'from', 'or', 'they', 'an', 'she', 'we', 'there', 'were',
    'one', 'all', 'do', 'if', 'so', 'my', 'when', 'their', 'them', 'would', 'will', 'no',
    'more', 'been', 'out', 'who', 'up', 'me', 'about', 'than', 'into', 'could', 'some',
    'what', 'can', 'just', 'him', 'now', 'any', 'like', 'other', 'then', 'its', 'only',
    'over', 'also', 'did', 'two', 'how', 'may', 'your', 'after', 'such', 'us', 'before',
    'most', 'these', 'must', 'much', 'through', 'again', 'each', 'many', 'down', 'off',
    'came', 'shall', 'should', 'our', 'those', 'under', 'might', 'last', 'going', 'new',
    'always', 'since', 'between', 'here', 'where', 'both', 'still', 'back', 'even',
    'because', 'make', 'does', 'go', 'went', 'too', 'yet', 'put', 'want', 'another',
    'while', 'every', 'thing', 'get', 'never', 'same', 'part', 'well', 'off', 'being'
])

filtered_words = [word for word in words if word not in stopwords]

word_counts = Counter(filtered_words)

most_common_words = word_counts.most_common(10)

for word, count in most_common_words:
    print(f'{word}: {count}')

'''


#Read the countries API and find
#the 10 largest countries
#the 10 most spoken languages
#the total number of languages in the countries API


import requests
url= "https://restcountries.com/v3.1/all"
response=requests.get(url)

text= response.json()

countries_area = [(country['name']['common'], country.get('area', 0)) for country in text]

largest_countries = sorted(countries_area, key=lambda x: x[1], reverse=True)[:10]

print("10 Largest Countries by Area:")
for country, area in largest_countries:
    print(f"{country}: {area} km²")

language_count = {}

for country in text:
    languages = country.get('languages', {}).values()
    for language in languages:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

most_spoken_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]


print("\n10 Most Spoken Languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count} countries")


total_languages = len(language_count)

print(f"\nTotal Number of Languages: {total_languages}")