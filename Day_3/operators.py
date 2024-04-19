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
