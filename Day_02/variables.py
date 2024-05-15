'''xercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line'''

#'Day 2: 30 Days of python programming'

first_name,last_name,full_name,country,city,age,year,is_married,is_true,is_light_on="Swapnil","Pardeshi","Swapnil N. Pardeshi","india","Nashik","30","2024",False,False,True


'''Exercises: Level 2
Check the data type of all your variables using type() built-in function'''

print(type(first_name),type(last_name),type(full_name),type(country),type(city),type(age),type(year),type(is_married),type(is_true),type(is_light_on))

#Using the len() built-in function, find the length of your first name

print(len(first_name))

#Compare the length of your first name and your last name

if len(first_name)>len(last_name):
    print("first name length is bigger")
else:
    print("last name length is bigger")


'''Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division'''

num_one,num_two=5,4

total=num_one + num_two
diff=num_one-num_two
product=num_one*num_two
division=num_one/num_two
remainder=num_two%num_one
exp=num_one**num_two
floor_division=num_one//num_two


'''The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.'''


radius=30
area_of_circle=3.14*radius**2
circum_of_circle=2*3.14*radius
print("area of cirle is",area_of_circle)
print("circumeference of circle is ",circum_of_circle) 

new_radius=int(input(("enter the radius")))
area_of_circle_new=3.14*new_radius**2
print("New radius entered area is", area_of_circle_new)


'''Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names'''
first_name=str(input("enter first name"))
last_name=str(input("enter last name"))
country=str(input("enter country name"))
age=int(input("enter the age"))

print(first_name,last_name,country,age)

print(help('keywords'))