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