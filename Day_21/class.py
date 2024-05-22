#Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]



import statistics
from collections import Counter
import math

class data:
    def __init__(self,lst):
        self.lst=lst
    
    def mean(self):
        return sum(self.lst)/len(self.lst)
    def median(self):
        n=len(self.lst)
        mid=n//2
        if n% 2 ==0:
            return(self.lst(mid-1) + self.lst(mid))/2
        else:
            return self.lst[mid]
    def mode(self):
        frequency=Counter(self.lst)
        mode_data=frequency.most_common()
        max_count = mode_data[0][1]
        modes = [num for num, freq in mode_data if freq == max_count]
        return modes
    def range(self):
        return max(self.lst) - min(self.lst)
    def variance(self):
        mean=self.mean()
        return sum((x-mean)**2 for x in self.data)/len(self.data)
    def standard_deviation(self):
        return math.sqrt(self.variance())
    def minimum(self):
        return min(self.lst)
    def maximum(self):
        return max(self.lst)
    def count(self):
        return len(self.lst)
    def percentile(self,percentile):
        index=(len(self.lst - 1) * (percentile/100.0))
        floor_index=math.floor(index)
        ceil_index=math.ceil(index)

        if floor_index==ceil_index:
            return self.data[int(index)]
        

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []  # List of tuples (amount, description)
        self.expenses = []  # List of tuples (amount, description)

    def total_income(self):
        return sum(amount for amount, _ in self.incomes)

    def total_expense(self):
        return sum(amount for amount, _ in self.expenses)

    def account_info(self):
        return f"Account Info:\nName: {self.firstname} {self.lastname}\nTotal Income: ${self.total_income():.2f}\nTotal Expense: ${self.total_expense():.2f}\nAccount Balance: ${self.account_balance():.2f}"

    def add_income(self, amount, description):
        self.incomes.append((amount, description))

    def add_expense(self, amount, description):
        self.expenses.append((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()

# Example Usage:
person = PersonAccount("John", "Doe")
person.add_income(5000, "Salary")
person.add_income(200, "Freelance Work")
person.add_expense(1500, "Rent")
person.add_expense(200, "Groceries")

print(person.account_info())
