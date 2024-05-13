# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique. 
"""
import random

def generate_unique_random_numbers():
    # Create an empty set to store unique numbers
    unique_numbers = set()

    # Generate random numbers until we have 7 unique ones
    while len(unique_numbers) < 7:
        unique_numbers.add(random.randint(0, 9))

    # Convert the set to a list and return
    return list(unique_numbers)

# Example usage:
random_numbers = generate_unique_random_numbers()
print(random_numbers)
"""

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(input_list):
    # Create a copy of the input list
    shuffled_list = input_list[:]
    
    # Shuffle the list
    random.shuffle(shuffled_list)
    
    return shuffled_list

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7]
shuffled = shuffle_list(my_list)
print(shuffled)