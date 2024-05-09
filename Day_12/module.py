#Writ a function which generates a six digit/character random_user_id.
  #print(random_user_id());
  #'1ee33d'
from random import random, randint

"""def random_user_id():
    id=randint(100000,999999)
    return id
print(f"random_user_id is {random_user_id()}")





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


#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
#print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)

    return r,g,b

print(rgb_color_gen())


# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
import string
def list_of_hexa_colors(num_colors):
    color_list = []
    for _ in range(num_colors):
        hex_code= "#" + ''.join(random.choices("0123456789abcdef",k=6))
        color_list.append(hex_code)
    return color_list


print(list_of_hexa_colors(5))


# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random

def list_of_rgb_colors(num_colors):
  
  Generates a list of the specified number of random RGB color codes.

  Args:
      num_colors (int): The number of colors to generate.

  Returns:
      list: A list of RGB color codes (strings) in the format "rgb(r, g, b)".
  

  color_list = []
  for _ in range(num_colors):
    # Generate random RGB values (0-255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = f"rgb({r}, {g}, {b})"  # Format as "rgb(r, g, b)"
    color_list.append(color_code)

  return color_list

# Example usage: Generate 3 random RGB colors
colors = list_of_rgb_colors(3)
print(colors)

"""

# Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(color):
  """Generates a list of random colors based on the specified type (hexa or rgb).

  Args:
      color (str): The type of color to generate ("hexa" or "rgb").

  Returns:
      list: A list of random color codes (strings).
  """

  # Inner functions for generating hexa and rgb colors
  if color == "hexa":
    def list_of_hexa_colors(num_colors):
      """Generates a list of random hexadecimal color codes."""
      color_list = []
      for _ in range(num_colors):
        hex_code = "#" + ''.join(random.choices("0123456789abcdef", k=6))
        color_list.append(hex_code)
      return color_list

  elif color == "rgb":
    def list_of_rgb_colors(num_colors):
      """Generates a list of random RGB color codes."""
      color_list = []
      for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_code = f"rgb({r}, {g}, {b})"
        color_list.append(color_code)
      return color_list

  else:
    raise ValueError("Invalid color type. Please choose 'hexa' or 'rgb'.")

  # Call the appropriate inner function based on the input color
  if color in ("hexa", "rgb"):
    return globals()[color]()  # Call the function dynamically using its name

# Example usage (without input):
colors = generate_colors("rgb")
print(colors)  # Output: (Example) ['rgb(12, 153, 101)', 'rgb(229, 57, 115)', ...]
