#Writ a function which generates a six digit/character random_user_id.
  #print(random_user_id());
  #'1ee33d'
from random import random, randint

def random_user_id():
    id=randint(100000,999999)
    return id
print(f"random_user_id is {random_user_id()}")



import random
import string

numberofchar=int(input("enter enumber of character"))
numberofid=int(input("enter number of ids"))


def generate_random_user_id():

    random_user_id=[]
    count = 0
    # Generate a random six-character user ID
    while count < numberofid:
        random_user_id.append(''.join(random.choices(string.ascii_letters + string.digits, k=numberofchar)))
        count += 1
    return random_user_id

# Test the function
print("Random User ID:", generate_random_user_id())


