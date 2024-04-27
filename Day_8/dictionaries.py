#Create an empty dictionary called dog

dog={}

#Add name, color, breed, legs, age to the dog dictionary

dog={
    'Name':'Labrodor',
    'Color':'Red',
    'Legs':4,
    'Age': 29
}

#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student={
    'first_name':'Swapnil',
    'last_name':'Pardeshi',
    'Gender':'Male',
    'Age':29,
    'Marital_status':'Single',
    'Skills':['Handsome','Good_Looking'],
    'Country':'India',
    'City':'Nashik',
    'Address':'Nashik'
}

#Get the length of the student dictionary

print(len(student))

#Get the value of skills and check the data type, it should be a list

print(student['Skills'],type(student['Skills']))

#Modify the skills values by adding one or two skills

student['Skills']=['Smart','Good','Mannered']

print(student['Skills'])

#Get the dictionary keys as a list

keys= student.keys()
print(keys)

#Get the dictionary values as a list

values=student.values()
print(values)

#Change the dictionary to a list of tuples using items() method

tuples=student.items()

print(tuples)

#Delete one of the items in the dictionary

del student['Age']

print(student)

#Delete one of the dictionaries

del student