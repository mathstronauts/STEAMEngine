# SEV and NEXUS - For Loops Sandwich Generator

from random import *

# sandwich lists
bread = ['white', 'whole wheat']  # index positions: white = 0, whole wheat = 1
meat = ['chicken', 'salami', 'bacon', 'tuna'] # index: chicken = 0, salami = 1, bacon = 2, tuna = 3
veggie = ['lettuce', 'tomato', 'onions', 'pickles', 'peppers', 'olives']

# message to users
print("Welcome to Random Sandwich Generator!")

num_veggie = input("How many veggies would you like on your sandwich? ")
num_meat = input("How many meats would you like on your sandwich? ")

print("Here is your sandwich!")
print(" ___________")
print("/___________\ ")

# print veggies
if num_veggie.lower() == "everything":
    for i in veggie:  # print every item in the list
        print (i)
else:
    for i in range(int(num_veggie)):  # generate a random number and print a certain number of times
        v = randint(0, len(veggie)-1)
        print(veggie[v])

# print meats
if num_meat.lower() == "everything":
    for i in meat:
        print (i)
else:
    for i in range(int(num_meat)):
        m = randint(0, len(meat) - 1)
        print(meat[m])

print("_____________")
print("\___________/")
