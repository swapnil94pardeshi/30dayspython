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


#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_even(start_no,end_no):
    addall=0
    for i in range(start_no,end_no):
        if i % 2==0:
            addall+=i
    return addall

print(sum_of_even(2,101))



#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    #print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

def evens_and_oddss(num):
    oddnum=0
    evennum=0
    for i in range(0,num):
        if i % 2 ==0:
            evennum+=1
        else:
            oddnum+=1
    return evennum,oddnum

print(evens_and_oddss(100))


#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number


def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

print(factorial(5))


#Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(data):
    if not data:
        return True
    else:
        return False

#Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mean(lst):
    addall=0
    for num in lst:
        addall+=num
    mean=addall/len(lst)

    return mean

def calculate_median(lst):
    lst.sort()
    middle=len(lst) // 2

    if len(lst)%2==0:
        median=lst[middle-1] + lst[middle] /2
    else:
        median=lst[middle]
    
    return median

from collections import Counter

def calculate_mode(lst):
    counts=Counter(lst)
    print(counts)
    max_frequency=max(counts.values())

    modes=[]

    for number,frequency in counts.items():
        if frequency ==max_frequency:
            modes.append(lst)
    
    return modes

def calculate_range(lst):
    if not lst:
        return "list is empty"
    
    max_value=max(lst)
    min_value=min(lst)

    range_value=max_value-min_value

    return range_value

def calculate_var(lst):
    if not lst:
        return "list is empty"
    
    mean=calculate_mean(lst)

    squared_diffs = [(x - mean) ** 2 for x in lst]

    variance = sum(squared_diffs) / len(lst)

    return variance

import math


def calculate_std(lst):
    if not lst:
        return "list is empty"
    
    variance=calculate_var(lst)

    stddeviation=math.sqrt(variance)

    return stddeviation


lst = [4, 8, 6, 2, 10]

print(calculate_mean(lst))
print(calculate_median(lst))
print(calculate_mode(lst))
print(calculate_range(lst))
print(calculate_var(lst))
print(calculate_std(lst))
'''

#Write a function called is_prime, which checks if a number is prime.

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True


print(is_prime(2))

#Write a functions which checks if all items are unique in the list.

lst = [4, 8, 6,6, 2, 10,"h"]

def isunique(lst):
    unique_set = set(lst)

    return len(unique_set) == len(lst)
print(isunique(lst))


#Write a function which checks if all the items of the list are of the same data type.

def checktype(lst):
    if not lst:
        return True
    data_type=type(lst[0])

    for i in lst[1:]:
        if type(i) != data_type:
            return False
        
    
    return True

print(checktype(lst))