import os

'''#Iterate 0 to 10 using for loop, do the same using while loop.
print("________________________________________________________")
for number in range(10):
    print(number)
print("______________________________________________________________")
n=0
while n <= 10:
    print(n)
    n=n+1

#Iterate 10 to 0 using for loop, do the same using while loop.

for number in range(10,-1,-1):
    print(number)

number=10

while number>=0:
    print(number)
    number-=1


#Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

for i in range(8,0,-1):
    print("#" *i)



#Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #


for i in range(8):
    for j in range(8):
        print("#", end='')
    print()

#Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100


for i in range(10):
    print(f"{i} x {i} = {i*i}")



#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

list_toiterate=['Python', 'Numpy','Pandas','Django', 'Flask']

for tech in list_toiterate:
    print(tech)



#Use for loop to iterate from 0 to 100 and print only even numbers


for even_number in range(0,100,2):
    print(even_number)


#Use for loop to iterate from 0 to 100 and print only odd numbers

for odd_number in range(0,100,1):
    print(odd_number)




#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#The sum of all numbers is 5050.


addall=0
for num in range(0,101):
    addall+=num
print(addall)



#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

#The sum of all evens is 2550. And the sum of all odds is 2500.
addalleven=0
addallodd=0

for num in range(0,101):
    if num%2== 0:
        addalleven+=num
    else:
        addallodd+=num
print(addalleven)
print(addallodd)


'''
#Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

import sys
import os

# Inside main.py

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))


from countries import countries

# Loop through the countries and extract those containing the word "land"
countries_with_land = [country for country in countries if "land" in country.lower()]

# Print the countries containing "land"
for country in countries_with_land:
    print(country)




#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
lst = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for fruits in lst[::-1]:
    reversed_fruits.append(fruits)
print(reversed_fruits)



# Go to the data folder and use the countries_data.py file.
#What are the total number of languages in the data
#Find the ten most spoken languages from the data
#Find the 10 most populated countries in the world

# Assuming countries_data.py defines a list of countries (Case 1)
# Or a dictionary with country data (Case 2)

# Inside main.py

# Importing countries data from countries_data.py file in the data folder




# Inside main.py

# Importing countries data from countries_data.py file in the data folder
from data.countries_data import countries

# Finding the ten most populated countries
most_populated_countries = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]

print("Ten most populated countries in the world:")
for country in most_populated_countries:
    print(country['name'], "-", country['population'])


