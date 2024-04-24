# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

string_to_print = "Thirty" +" "+ "Days" +" " + "Of" + " " + "Python"
print(string_to_print)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

string_to_print_1= "Coding" + " " + "For" + " " + "All"
print(string_to_print_1)

#Declare a variable named company and assign it to an initial value "Coding For All".

Company= "Brahmand Edutech"
string_to_print_2= Company + " " + "Coding For All"
print(string_to_print_2)

#Print the variable company using print().


print("Brahmand Edutech")

#Print the length of the company string using len() method and print().

print( f" {len(Company)}  {Company} " )


# Change all the characters to uppercase letters using upper() method.

Company = Company.upper()

print(Company)

# Change all the characters to lowercase letters using lower() method.

Company_lower= Company.lower()

print(Company_lower)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

Company_cap= Company. capitalize()
Company_title = Company. title()
Company_swap = Company. swapcase()

print(Company_cap , Company_title , Company_swap)

# Cut(slice) out the first word of Coding For All string.

company_split=Company.split()

print(company_split[0])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

