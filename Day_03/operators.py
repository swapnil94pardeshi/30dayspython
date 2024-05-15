'''

#Declare your age as integer variable

age=int(10)

#Declare your height as a float variable
height=float(170.5)

#Declare a variable that store a complex number
complex_number=complex(3,4)

#Write a script that prompts the user to enter base and height of the triangle. calculate an area of this triangle (area = 0.5 x b x h).

base_of_triangle,height_of_triangle=float(input("Enter base of traingle ")),float(input("enter height of triangle "))

area_of_triangle=(0.5*base_of_triangle*height_of_triangle)
print("Area of Triangle is ", area_of_triangle)


#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

side_a,side_b,side_c=float(input("enter side A ")), float(input("enter side B ")), float(input("enter side C "))

perimeter_of_triangle=(side_a+side_b+side_c)
print("Perimeter of Triangle is ", perimeter_of_triangle)


#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length_of_rectangle,width_of_rectangle=float(input("ENter length ")), float(input("enter width "))

area_of_rectangle=(length_of_rectangle*width_of_rectangle)

perimeter_of_rectangle=(2*(length_of_rectangle + width_of_rectangle))

print(f"area of rectangle is {area_of_rectangle} , and perimeter of rectangle is  {perimeter_of_rectangle}") 



#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius_of_circle=float(input("enter radius of circle "))

area_of_circle=3.14*radius_of_circle**2
circumference_of_circle=2*3.14*radius_of_circle

print(f"area of circle is {area_of_circle} and circumference of circle is {circumference_of_circle}")


#Calculate the slope, x-intercept and y-intercept of y = 2x -2

equation = "y = 2x - 2"

equation_parts = equation.split("=")

print(equation_parts)

y_part, mx_part = equation_parts

print(y_part,mx_part)

m_coefficient, x_term = mx_part.split("x")

print(m_coefficient,x_term)

m = float(m_coefficient.strip())
b = float(x_term.strip().split("-")[-1])

print(m,b)

x_intercept = -b / m
print(x_intercept)


#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
point1 = (2, 2)
point2 = (6, 10)

slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
euclidean_distance = math.dist((2, 2), (6,10))
print(euclidean_distance, slope)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x=(-5,-4,-3,-2,-1,0,1,2,3,4,5)

for value in x:
    y=value*value + 6*value + 9
    if y==0:
        print(value)


#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len_1=len("python")
len_2=len("dragon")

if len_1 != len_2:
    print("falsy comparison")



#Use and operator to check if 'on' is found in both 'python' and 'dragon'

word1="python"
word2="dragon"

both_contain="on" in word1 and "on" in word2

print(both_contain)


#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence="I hope this course is not full of jargon."

ispresent="jargon" in sentence
print(ispresent)


#Find the length of the text python and convert the value to float and convert it to string

len1=len("python")
convertfloat=float(len1)
convertstr=str(convertfloat)

print(convertstr, type(convertstr))



#17 Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

num=int(input("enter the number of your choice "))

if num % 2== 0:
    print("number is even")
else:
    print("number is odd")

    

# 18 Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
valuecheck=int(2.7)
floordivision=7//3

if valuecheck==floordivision:
    print("values are equal")
else:
    print("values are not equal")



# 19 Check if type of '10' is equal to type of 10

value1="10"
value2=10

if type(value1) == type(value2):
    print("type are equal")
else:
    print("type are not equal")




# 20 Check if int('9.8') is equal to 10

value1=int(9.8)
value2= 10

if value1 == value2:
    print("values are equal")
else:
    print("values are not equal")


# 21 Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours=int(input("enter number of hours "))
rate_per_hour=float(input("enter rate per hour "))

pay_of_person= hours * rate_per_hour

print(pay_of_person)



# 22 Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years=int(input("Enter number of years you have lived: "))
numbers_of_seconds=years*31536000

print(f"You have lived for {numbers_of_seconds} seconds.")



#23Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''

def generate_table(rows):
  """Generates a table showing powers of numbers.

  Args:
      rows: Number of rows in the table.

  Returns:
      A list of lists representing the table data.
  """
  table = []
  for i in range(1, rows + 1):
    row = [i]  # Start each row with the base number
    for j in range(1, 5):
      power = i ** j  # Calculate the power
      row.append(power)
    table.append(row)
  return table

# Define the number of rows
rows = 5

# Generate the table data
table_data = generate_table(rows)

# Print the table with formatted output
for row in table_data:
  for value in row:
    print(f"{value:4}", end=" ")  # Format each value with 4 spaces
  print()  # Print a newline after each row

