# importing modules
import random 
import string

# declaring variables
lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
characters = string.punctuation

# generating the password
all_elements = lower + upper + number + characters
length = 37
the_pass = "".join(random.sample(all_elements, length))
