it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies

print(len(it_companies))

#Add 'Twitter' to it_companies

it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies

it_companies.update({'Brahmand','Offersindia'})
print(it_companies)

#Remove one of the companies from the set it_companies

it_companies.remove('Apple')

print(it_companies)


#What is the difference between remove and discard

# Join A and B

c= A.union(B)
print(c)

# Find A intersection B

D= A.intersection(B)
print(D)

#Is A subset of B

print(A.issubset(B))

#Are A and B disjoint sets

print(A.isdisjoint(B))

#Join A with B and B with A

E=A.union(B)
print(E)

F=B.union(A)
print(F)

#Delete the sets completely
del A
del B


#Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set=set(age)

print(len(age),len(age_set))


# Explain the difference between the following data types: string, list, tuple and set

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

string="I am a teacher and I love to inspire and teach people"

list_of_words=string.split(" ")
print (list_of_words)

set_of_words=set(list_of_words)

print(set_of_words)