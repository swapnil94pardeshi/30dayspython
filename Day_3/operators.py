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
'''
#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x=(-5,-4,-3,-2,-1,0,1,2,3,4,5)

for value in x:
    y=value*value + 6*value + 9
    if y==0:
        print(value)
