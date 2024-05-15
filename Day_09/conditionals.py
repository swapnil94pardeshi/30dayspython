'''#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#Enter your age: 30
#You are old enough to learn to drive.
#Output:
#Enter your age: 15
#You need 3 more years to learn to drive.

age=int(input("Enter Your Age"))

if age>=18:
    print("You are old enough to drive.")
else:
    print(f"You need {18-age} more years to learn to drive")


#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#Enter your age: 30
#You are 5 years older than me.

your_age=int(input("Enter your age"))

if age==your_age:
    print("we are of same age")
elif age>your_age:
    print("I am older than you")
else :
    print("you are older than")


#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
#Enter number one: 4
#Enter number two: 3
#4 is greater than 3

Number_one=int(input("Enter first number "))
Number_two=int(input("Enter Second Number "))

if Number_one > Number_two:
    print("Number One is Greater than number two")
elif Number_one < Number_two:
    print("Number two is greater than number one")
else:
    print("Number one is equal to number two")


#Write a code which gives grade to students according to theirs scores:
#80-100, A
#70-80, B
#60-69, C
#50-59, D
#0-49, F

marks=int(input("Enter your marks "))

if marks>80 and marks <100:
    print("A")
elif marks>70 and marks<80:
    print(" B")
elif marks>60 and marks<69:
    print(" C")
elif marks>50 and marks<59:
    print(" D")
elif marks>0 and marks<49:
    print(" F")




#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month=(input("enter month ")).lower()

autumn=("september","octomber","november")
winter=("december","january","february")
spring=("march","april","may")
summer=("june","july","august")
if month in autumn:
    print("The season is autumn")
elif month in winter:
    print("The Seasion is winter")
elif month in spring:
    print("The season is spring")
elif month in summer:
    print(" The Season is Summer")
else:
    print("enter right month")



#The following list contains some fruits:
fruit=(input("enter fruit ")).lower()
fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

if fruit in fruits:
    print(f"{fruit} fruit already exist in list {fruits}")
else:
    fruits.append(fruit)
    print(f"updated list of fruits is {fruits}")
'''


# Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
}
 #* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 #* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 #* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 #* If the person is married and if he lives in Finland, print the information in the following format:


key= person.keys

if 'skills' in person:
     skills=person['skills']
     print((skills[int(len(skills) /2)]))
if "python" in skills:
    print("The person has the 'Python' skill.")
else:
    print("The person does not have the 'Python' skill.")


frontend_skills = {'JavaScript', 'React'}
backend_skills = {'Node', 'Python', 'MongoDB'}
fullstack_skills = frontend_skills.union(backend_skills)



if fullstack_skills.issubset(skills):
    print("He is a fullstack developer")
elif frontend_skills.issubset(skills) and len(skills) == len(frontend_skills):
    print("He is a frontend developer")
elif backend_skills.issubset(skills):
    print("He is a backend developer")
else:
    print(" no title found")