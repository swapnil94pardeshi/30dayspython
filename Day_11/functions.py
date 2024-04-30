# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def sum_two(num1,num2):
    add=num1+num2
    return add

print(sum_two(10,20))

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(radius):
    area=3.14*radius*radius
    return area

print(area_of_circle(10))



#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total=0
    for num in nums:
        if isinstance(num,(int,float)):
            total+=num
        else:
            return"error:all items must be numeric"
    return total    

print(add_all_nums(1,2,3,4,5))


#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    f=(celsius*(9/5)) + 32
    return f

print(convert_celsius_to_fahrenheit(1))


#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer

def check_season(month):
    month=month.lower()
    autumn=['september','october','november']   
    winter=("december","january","february")
    spring=("march","april","may")
    summer=("june","july","august")
    if month in autumn:
        print("Autumn")
    elif month in winter:
        print("winter")
    elif month in spring:
        print("spring")
    elif month in summer:
        print("summer")


check_season("January")



# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,x2,y1,y2):
    if x2-x1==0:
        return "error division by zero"
    slope=(y2-y1)/(x2-x1)
    return slope

print(calculate_slope(1,2,3,4))



# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math
def solve_quadratic_eqn(a,b,c):
    abss=b*b-(4*a*c)
    sol1=-b+(math.sqrt(abss))/2*a
    sol2=-b-(math.sqrt(abss))/2*a
    return sol1,sol2

print(solve_quadratic_eqn(1,4,3))