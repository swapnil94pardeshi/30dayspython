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

from ..countries import countries

print(countries.countries)


#countries_with_land = [country.lower() for country in countries.countries if "land" in country.lower()]

#print(countries_with_land)
#for country in countries.countries:
 #   if "land" in country:
  #      print(country)
