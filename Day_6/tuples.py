#Create an empty tuple

first_tuple=()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

first_tuple=("Swapnil","diksha","Kajal")
second_tuple=("Diksha1","Kajal")
print(first_tuple)

# Join brothers and sisters tuples and assign it to siblings

siblings_tuple= first_tuple + second_tuple

print(siblings_tuple)

#How many siblings do you have?

print(len(siblings_tuple))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members

list_sibling_tuples=list(siblings_tuple)

list_sibling_tuples.append("Mother")
list_sibling_tuples.append("Father")

print(list_sibling_tuples)

tuple_list_sibling_tuples=tuple(list_sibling_tuples)

print(tuple_list_sibling_tuples)

#Unpack siblings and parents from family_members

list_sibling_tuples_sibling=list_sibling_tuples[:5]
list_sibling_tuples_parents=list_sibling_tuples[5:]

print(list_sibling_tuples_sibling)
print(list_sibling_tuples_parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits=['apples','oranges','kiwi','guava','mango']
vegetables=['spinach','fenugreek','lady finger']
animal_products=['milk','curd','dairy']

food_stuff_tp=fruits + vegetables + animal_products

print(food_stuff_tp)


#Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt=list(food_stuff_tp)

print(food_stuff_lt)


#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

middle_item=food_stuff_lt[int(len(food_stuff_lt)/2)]

print(middle_item)

#Slice out the first three items and the last three items from food_staff_lt list

first_three= food_stuff_lt[0:3]
last_three=food_stuff_lt[-3:]

print(first_three,  last_three)

#Delete the food_staff_tp tuple completely

del food_stuff_tp
# print(food_stuff_tp)

# Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country

#Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

