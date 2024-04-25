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

#Print the first, middle and last company


print(it_companies[0],it_companies[int(len(it_companies)/2)],it_companies[-1])

#Print the list after modifying one of the companies

it_companies.append("Brahmand")

print(it_companies)

#Add an IT company to it_companies

#Insert an IT company in the middle of the companies list


it_companies.insert(int(len(it_companies)/2),"Offersindia")

print(it_companies)


#Change one of the it_companies names to uppercase (IBM excluded!)


it_companies[-1]=it_companies[-1].upper()

print(it_companies)

#Join the it_companies with a string '#;  

joined_companies="# ".join(it_companies) + ";"

print(joined_companies)

#Check if a certain company exists in the it_companies list.

if_present="Brahmand" in it_companies

print(if_present)

#Sort the list using sort() method
it_companies.sort()

print(it_companies)

#Reverse the list in descending order using reverse() method

it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list

first3=it_companies[0:3]
print(first3)

#Slice out the last 3 companies from the list

last3=it_companies[-3:]
print(last3)

#Slice out the middle IT company or companies from the list
middle_company=it_companies[int(len(it_companies)/2)]
print(middle_company)

#Remove the first IT company from the list

del it_companies[0]
print(it_companies)

#Remove the middle IT company or companies from the list

del it_companies[int(len(it_companies)/2)]

print(it_companies)

# Remove the last IT company from the list

del it_companies[-1]

print(it_companies)

#Remove all IT companies from the list

it_companies.clear()

print(it_companies)

#Destroy the IT companies list

del it_companies



# Join the following lists:
#front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#back_end = ['Node','Express', 'MongoDB']
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joinedlist= front_end + back_end
print(joinedlist)



# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack=joinedlist.copy()

print(full_stack)

index= full_stack.index("Redux")
full_stack.insert(index+1, "Python")
full_stack.insert(index+2,"SQL")
print(full_stack)