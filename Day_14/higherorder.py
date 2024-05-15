countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Use for loop to print each country in the countries list.

for country in countries:
    print(country)

#Use for to print each name in the names list.

for name in names:
    print(name)

#Use for to print each number in the numbers list.
for num in numbers:
    print(num)


# Use map to create a new list by changing each country to uppercase in the countries list


uppercase_letters= map(lambda name:name.upper(),countries)

print(list(uppercase_letters))

# Use map to create a new list by changing each number to its square in the numbers list

squares_numbers= map(lambda num:num*num,numbers)
print(list(squares_numbers))

#Use map to change each name to uppercase in the names list
uppercase_name=map(lambda name:name.upper(),names)

print(list(uppercase_name))

#Use filter to filter out countries containing 'land'.

name_in_land= filter(lambda name:"land" in name ,countries)

print(list(name_in_land))

#Use filter to filter out countries having exactly six characters.

name_greater_than_six= filter(lambda name:len(name) == 6,countries)

print(list(name_greater_than_six))

#Use filter to filter out countries containing six letters and more in the country list.

name_greater_than_six_or_more= filter(lambda name:len(name) >= 6,countries)

print(list(name_greater_than_six_or_more))

# Use filter to filter out countries starting with an 'E'

countries_with_e=filter(lambda name:name.startswith("E"),countries)

print(list(countries_with_e))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

from functools import reduce

# Define a list
numbers = [1, 2, 3, 4, 5]

# Chain map, filter, and reduce
result = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers)))

print(result)  # Output: 24

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
mixed_string=["apple","guava",1,"peru",3,4,"simple"]
def get_string_lists():
    return list(filter(lambda name:isinstance(name,str),mixed_string))
print((get_string_lists()))

# Use reduce to sum all the numbers in the numbers list.

print(reduce(lambda x,y:x+y,numbers))

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
lst=reduce(lambda x,y:x+(", ")+y,countries)
print(f"{lst} are north European countires" )

#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).


import countries

def categorize_countries():
    return filter(lambda name:"land" in name,countries.countries1)

print(list(categorize_countries()))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
import countries_data
def returncountry():
    initial_counts = {}
    for country in countries.countries1:
        initial = country[0].upper()  # Get the first letter and convert to uppercase
        initial_counts[initial] = initial_counts.get(initial, 0) + 1  # Increment the count for the initial
    return initial_counts

print(returncountry())


#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

def get_first_10_countries():
    count=0
    country12=[]
    
    for country in countries.countries1:
        if count<= 10:
            country12.append(country)
            count+=1
    return country12

print(get_first_10_countries())

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

def last_ten_countries():
    return countries.countries1[-11:]

print(last_ten_countries())



#Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#Sort countries by name, by capital, by population
#Sort out the ten most spoken languages by location.
#Sort out the ten most populated countries.

import countries_data

countries_sorted_by_name = sorted(countries_data.countries21, key=lambda x: x['name'])

print("Countries sorted by name:")
for country in countries_sorted_by_name:
    print(country['name'])


countries_sorted_by_capital = sorted(countries_data.countries21, key=lambda x: x['capital'])

print("\nCountries sorted by capital:")
for country in countries_sorted_by_capital:
    print(country['name'], "-", country['capital'])

# Sort countries by population
countries_sorted_by_population = sorted(countries_data.countries21, key=lambda x: x['population'], reverse=True)

print("\nCountries sorted by population:")
for country in countries_sorted_by_population:
    print(country['name'], "-", country['population'])


languages_spoken = {}
for country in countries_data.countries21:
    for language in country['languages']:
        languages_spoken[language] = languages_spoken.get(language, 0) + 1

top_spoken_languages = sorted(languages_spoken.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_spoken_languages)


top_populated_countries = sorted(countries_data.countries21, key=lambda x: x['population'], reverse=True)[:10]

print(top_populated_countries)



