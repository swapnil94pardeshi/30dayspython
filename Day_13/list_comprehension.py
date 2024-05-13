#Filter only negative and zero in the list using list comprehension
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

positive_numbers=[i for i in numbers if i > 0]
print(positive_numbers)

#Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]
print(flattened_list)

#output [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)] 

numbers = [(i,1, i,i**2,i**3,i**4,i**5) for i in range(11)]
print(numbers) 


#Flatten the following list to a new list:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

flattened_list = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]

print(flattened_list)



#Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#output:
#[{'country': 'FINLAND', 'city': 'HELSINKI'},
#{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#{'country': 'NORWAY', 'city': 'OSLO'}]

list_of_dictionaries=[{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

print(list_of_dictionaries)



#Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output = ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

output=[fname + " " + lname for sublist in names for fname,lname in sublist]

print(output)

"""

#Write a lambda function which can solve a slope or y-intercept of linear functions.

slope=lambda x1,x2,y1,y2,solve_for:(y2-y1)/(x2-x1) if solve_for=='slope1' else y1 - ((y2 - y1) / (x2 - x1)) * x1
slope1=slope(1,2,3,4,'slope')
y_intercept=slope(1,2,3,4,'y_intercept')

print(slope1)
print(y_intercept)

