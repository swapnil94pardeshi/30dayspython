#Check the python version you are using
import sys
print(sys.version)


'''Open the python interactive shell and do the following operations. The operands are 3 and 4.
addition(+)
subtraction(-)
multiplication(*)
modulus(%)
division(/)
exponential(**)
floor division operator(//) '''

a,b=3,4

print("sum is", a+b)
print("substraction is", a-b)
print("multiplication is", a*b)
print("modulus is", a%b)
print("Division is", a/b)
print("Exponential is", a**b)
print("Floor division operator is", a//b)




'''Write strings on the python interactive shell. The strings are the following:
Your name
Your family name
Your country
I am enjoying 30 days of python'''

Your_name,Your_family_name,Your_country= "Swapnil N. Pardeshi" , "Pardeshi", "India"

print("my name is",Your_name)
print("My Family Name is", Your_family_name)
print("My Country is",Your_country)
print("i am enjoying 30 days of python")




'''Check the data types of the following data:
10
9.8
3.14
4 - 4j
['Asabeneh', 'Python', 'Finland']
Your name
Your family name
Your country'''


print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(Your_name))
print(type(Your_family_name))
print(type(Your_country))



'''Find an Euclidian distance between (2, 3) and (10, 8)'''

import math
print(math.dist((2, 3),(10, 8)))