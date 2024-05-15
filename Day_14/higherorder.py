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