# beginner SEV - import random library

import random

random_num = random.randint(1, 10)
# randint(lowerlimit, upperlimit)
# randint stands for "random integer" - it will give us a random whole number within the specified range

# message to users
print("Try to guess what number I am thinking of!")
guess = input("Please enter a number: ")

print("My number was:", str(random_num))  # remember to convert the number to a string to print
