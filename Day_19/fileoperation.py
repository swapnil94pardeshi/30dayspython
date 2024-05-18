#Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
'''
    
def count_words_in_list(text_list):
    total_words = 0
    for text in text_list:
        words = text.split()
        total_words += len(words)
    return total_words


file_path=['D:/Python/30day/data/obama_speech.txt','D:/Python/30day/data/michelle_obama_speech.txt','D:/Python/30day/data/melina_trump_speech.txt','D:/Python/30day/data/donald_speech.txt']

for file in file_path:
    with open(file) as f:
        lines = f.readlines()
        print(f" Number of lines in {file} is {len(lines)}")
        print(f" & Number of words are {count_words_in_list(lines)}")


#Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages


import json
from collections import Counter

file_path= 'D:/Python/30day/data/countries_data.json'

def find_ten_most_spoken_languages(file_path):
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        countries_data = json.load(file)
    
    # Initialize a Counter object to count the languages
    language_counter = Counter()

    # Iterate through each country's data to extract and count languages
    for country in countries_data:
        languages = country.get('languages', [])
        for language in languages:
            language_counter[language] += 1
    
    most_common_languages = language_counter.most_common(10)

    return most_common_languages


top_ten_languages = find_ten_most_spoken_languages(file_path)
print("The ten most spoken languages are:")
for language, count in top_ten_languages:
    print(f"{language}: {count}")




import json

# Define the function to read the JSON file and find the ten most populated countries
def find_ten_most_populated_countries(file_path):
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        countries_data = json.load(file)
    
    # Create a list of tuples containing country name and population
    country_population = [(country['name'], country['population']) for country in countries_data]

    # Sort the list by population in descending order
    country_population.sort(key=lambda x: x[1], reverse=True)

    # Get the top ten most populated countries
    top_ten_populated_countries = country_population[:10]

    return top_ten_populated_countries

# Specify the path to the JSON file
file_path = 'D:/Python/30day/data/countries_data.json'

# Call the function and print the result
top_ten_populated_countries = find_ten_most_populated_countries(file_path)
print("The ten most populated countries are:")
for country, population in top_ten_populated_countries:
    print(f"{country}: {population}")



#Extract all incoming email addresses as a list from the email_exchange_big.txt file.

import re

def extract_email_addresses(file_path):
    # Regular expression for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Initialize an empty list to store email addresses
    email_addresses = []

    # Read the contents of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Find all email addresses using the regular expression
        email_addresses = re.findall(email_pattern, content)
    
    return email_addresses

# Specify the path to the email exchange file
file_path = 'D:/Python/30day/data/email_exchanges_big.txt'

# Call the function and print the result
email_addresses = extract_email_addresses(file_path)
print("Extracted email addresses:")
for email in email_addresses:
    print(email)




#Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

import re
from collections import Counter

def find_most_common_words(input_data,number_of_words):
    def process_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation using regex
        text = re.sub(r'[^\w\s]', '', text)
        # Split text into words
        words = text.split()
        return words
    
    if isinstance(input_data, str) and input_data.endswith('.txt'):
        # Read the file content
        with open(input_data, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        # Use the input_data as text directly
        text = input_data
     # Process the text to get words
    words = process_text(text)
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_common = word_counts.most_common(number_of_words)
    
    return [(count, word) for word, count in most_common]


result = find_most_common_words('D:/Python/30day/data/obama_speech.txt', 10)
print(result)



#Use the function, find_most_frequent_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech



import re
from collections import Counter

def find_most_common_words(input_data,number_of_words):
    def process_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation using regex
        text = re.sub(r'[^\w\s]', '', text)
        # Split text into words
        words = text.split()
        return words
    
    if isinstance(input_data, str) and input_data.endswith('.txt'):
        # Read the file content
        with open(input_data, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        # Use the input_data as text directly
        text = input_data
     # Process the text to get words
    words = process_text(text)
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_common = word_counts.most_common(number_of_words)
    
    return [(count, word) for word, count in most_common]


result = find_most_common_words('D:/Python/30day/data/obama_speech.txt', 10)
print(result)



#Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory


import re
import numpy as np
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

def clean_text(text):
    """Cleans the text by removing punctuation and converting to lowercase."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def remove_support_words(text, stop_words):
    """Removes stop words from the text."""
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_words)

def read_file(file_path):
    """Reads text from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def check_text_similarity(text1, text2, stop_words):
    """Evaluates the similarity between two cleaned texts."""
    # Clean the texts
    text1_clean = clean_text(text1)
    text2_clean = clean_text(text2)
    
    # Remove stop words
    text1_no_stop = remove_support_words(text1_clean, stop_words)
    text2_no_stop = remove_support_words(text2_clean, stop_words)
    
    # Use TF-IDF Vectorizer to calculate similarity
    vectorizer = TfidfVectorizer().fit_transform([text1_no_stop, text2_no_stop])
    vectors = vectorizer.toarray()
    cosine_similarity = np.dot(vectors[0], vectors[1]) / (np.linalg.norm(vectors[0]) * np.linalg.norm(vectors[1]))
    
    return cosine_similarity

# Example usage
text_file_path1 = 'D:/Python/30day/data/michelle_obama_speech.txt'  # Path to the first text file
text_file_path2 = 'D:/Python/30day/data/melina_trump_speech.txt'    # Path to the second text file

# Load stop words from the module
stop_words = set(stop_words)

# Read texts from files
text1 = read_file(text_file_path1)
text2 = read_file(text_file_path2)

# Check similarity
similarity = check_text_similarity(text1, text2, stop_words)
print(f"Similarity between the two texts: {similarity:.2f}")




#Find the 10 most repeated words in the romeo_and_juliet.txt


import re
from collections import Counter

def find_most_common_words(input_data,number_of_words):
    def process_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation using regex
        text = re.sub(r'[^\w\s]', '', text)
        # Split text into words
        words = text.split()
        return words
    
    if isinstance(input_data, str) and input_data.endswith('.txt'):
        # Read the file content
        with open(input_data, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        # Use the input_data as text directly
        text = input_data
     # Process the text to get words
    words = process_text(text)
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the most common words
    most_common = word_counts.most_common(number_of_words)
    
    return [(count, word) for word, count in most_common]


result = find_most_common_words('D:/Python/30day/data/romeo_and_juliet.txt', 10)
print(result)


'''


#Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript

import csv

def count_keywords_in_csv(csv_file_path, keyword1, keyword2=None):
    count_keyword1 = 0
    count_keyword2 = 0

    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row['title'].lower()
            if keyword1.lower() in title:
                count_keyword1 += 1
            if keyword2 and keyword2.lower() in title:
                count_keyword2 += 1

    return count_keyword1, count_keyword2

# CSV file path
csv_file_path = 'D:/Python/30day/data/hacker_news.csv'

# Part (a): Count lines containing Python or python
python_count, _ = count_keywords_in_csv(csv_file_path, 'python')

# Part (b): Count lines containing JavaScript, javascript, or Javascript
javascript_count, _ = count_keywords_in_csv(csv_file_path, 'javascript', 'javascript')

# Part (c): Count lines containing Java and not JavaScript
java_count, _ = count_keywords_in_csv(csv_file_path, 'java', 'javascript')

print(f"Number of lines containing Python: {python_count}")
print(f"Number of lines containing JavaScript: {javascript_count}")
print(f"Number of lines containing Java and not JavaScript: {java_count}")  


