"""# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

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
print(Company)
try:
    check=Company.index("BRAHMANd")
    print(f" word found at {check} index")
except ValueError:
    print("word not found")

Company="Brahmand Edutech"
try:
    checkfind=Company.find("BRAHMAND")
    print(f"Word found at {checkfind} index")
except ValueError:
    print("word not found")


Company="Brahmand Edutech"


# Replace the word coding in the string 'Coding For All' to Python.
Company=Company.replace("Brahmand", "BRAHMAND")
print(Company)

#Change Python for Everyone to Python for All using the replace method or other methods.

Company=Company.replace("BRAHMAND","Brahmand Edutech!!!!!")
print(Company)

#Split the string 'Coding For All' using space as the separator (split()) .
Company="Coding For All"
Company=Company.split(" ")
print(Company)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
newstring="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
newstring=newstring.split(",")
print(newstring)
"""

#What is the character at index 0 in the string "Coding For All."
newstring="Coding For All"
charat=newstring[0]

print(charat)

#What is the last index of the string Coding For All.

lastchar=newstring[-1]
print(lastchar)

#What character is at index 10 in "Coding For All" string.
charat10=newstring[10]
print(charat10)

#Create an acronym or an abbreviation for the name 'Python For Everyone'.

name = "Python For Everyone"
acronym=""
for word in name.split(" "):
    acronym+=word[0].upper()

print(acronym)

#Create an acronym or an abbreviation for the name 'Coding For All'.

nameabbr="Coding For All"
acronym1=""
for word in nameabbr.split(" "):
    acronym1+=word[0].upper()

print(acronym1)

#Use index to determine the position of the first occurrence of C in Coding For All.

indexfirst=nameabbr.index("C")

print(indexfirst)

# Use index to determine the position of the first occurrence of F in Coding For All.

indexf=nameabbr.index("F")

print(indexf)

#Use rfind to determine the position of the last occurrence of l in Coding For All People.

indexl=nameabbr.rfind("L")
print(indexl)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence='You cannot end a sentence with because because because is a conjunction'
occurbecuase=sentence.index("because")
occurbecuase1=sentence.find("because")

print(occurbecuase)
print(occurbecuase1)

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence='You cannot end a sentence with because because because is a conjunction'

occurbecuasee=sentence.rindex("because")

print(occurbecuasee)


#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence='You cannot end a sentence with because because because is a conjunction'
startindex=sentence.find("because")
endindex=sentence.find("is")
slicedsentence=sentence[startindex:endindex]

print(slicedsentence)


#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(startindex)


#Does ''Coding For All' start with a substring Coding?

string="Coding For ALL"
substring=string.split(" ")
if substring[0] == "Coding":
    print("Substring is Matched")
else:
    print("substring does not matched")

#Does 'Coding For All' end with a substring coding?
string="Coding For ALL"
substring=string.split(" ")
if substring[-1] == "Coding":
    print("Substring is Matched")
else:
    print("substring does not matched")

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
trimstring='   Coding For All      '
trimstring=trimstring.strip()
print(trimstring)

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python

string1=["30DaysOfPython","thirty_days_of_python"]
for word in string1:
    if word.isidentifier():
        print(f"{word}  is an identifier")
    else: 
        print(f"{word}  is not identifier")


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

pythonlibrary=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
pythonlibrary.append('Hash')
print(pythonlibrary)

# Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
separatesequence="I am enjoying this challenge. \n I just wonder what is next."

print(separatesequence)

#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki

print("Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki")

#Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.

print(f"radius = 10\narea = 3.14 * radius **2\nThe area of a circle with radius 10 is 314 meters square")

#Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144

#print(f"{8 + 6 = 14}\n{8 - 6 = 2}\n{8 * 6 = 48}\n{8 / 6 = 1.33}\n{8 % 6 = 2}\n{8 // 6 = 1}\n{8 ** 6 = 262144}")

num1 = 8
num2 = 6

# Addition
print(f"{num1} + {num2} = {num1 + num2}")

# Subtraction
print(f"{num1} - {num2} = {num1 - num2}")

# Multiplication
print(f"{num1} * {num2} = {num1 * num2}")

# Division with two decimal places
print(f"{num1} / {num2} = {num1 / num2:.2f}")

# Modulo
print(f"{num1} % {num2} = {num1 % num2}")

# Floor division
print(f"{num1} // {num2} = {num1 // num2}")

# Exponentiation
print(f"{num1} ** {num2} = {num1 ** num2}")
