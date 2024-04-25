fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

print("fruits",fruits)

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst

print(first_item)

# Declare an empty list

empty_list=[]

# Declare a list with more than 5 items

items5=['a','b','c','d','e']

#Find the length of your list

print(len(items5))

# Get the first item, the middle item and the last item of the list

first_item1=items5[0]
middle_item=items5[int(len(items5)/2)]
last_item=items5[-1]

print(first_item1,middle_item,last_item)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types=["Swapnil",29,5.10,"single","Nashik Road"]

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#Print the list using print()
print(it_companies)

#Print the number of companies in the list

print(len(it_companies))