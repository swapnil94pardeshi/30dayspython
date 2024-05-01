'''# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

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


#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(lst):
    for i in lst:
        print(i)

print_list([1,2,3,4,5])

#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lst):
    reversed_array=[]
    for i in range(len(lst)-1,-1,-1):
        reversed_array.append(lst[i])
    return reversed_array

print(reverse_list([1,2,3,4,5]))

#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    capital=[]
    for i in lst:
        capital.append(i.capitalize())
    return capital


print(capitalize_list_items(['swap','ram','sham']))


#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
#print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
#print(add_item(numbers, 5))      [2, 3, 7, 9, 5]


def add_item(lst,item):
    lst.append(item)
    print(lst)

add_item(food_staff,"raw")

print(food_staff)


#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

#print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];

#print(remove_item(numbers, 3))  # [2, 7, 9]


def remove_item(lst,name_to_remove):
  
    for i in lst:
        if i==name_to_remove:
            lst.remove(i)
    return lst

print(remove_item(food_staff,"Potato"))

print(food_staff)


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
#print(sum_of_numbers(5))  # 15
#print(sum_all_numbers(10)) # 55
#print(sum_all_numbers(100)) # 5050


def sum_of_numbers(*args):
    addall=sum(args)
    return addall

print(sum_of_numbers(5,10,15))

#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(start_no,end_no):
    addall=0
    for i in range(start_no,end_no):
        if i % 2!=0:
            addall+=i
    return addall

print(sum_of_odds(2,100))
'''

#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(start_no,end_no):
    addall=0
    for i in range(start_no,end_no):
        if i % 2==0:
            addall+=i
    return addall

print(sum_of_even(2,101))
