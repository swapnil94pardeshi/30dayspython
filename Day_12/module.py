#Writ a function which generates a six digit/character random_user_id.
  #print(random_user_id());
  #'1ee33d'
from random import random, randint

def random_user_id():
    id=randint(100000,999999)
    return id
print(f"random_user_id is {random_user_id()}")


