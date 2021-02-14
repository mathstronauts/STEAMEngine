# Advanced NEXUS - Function Random Index

import random

# random selection function
def random_selector(List):
    a = random.randint(0, len(List) - 1)
    return List[a]

# sandwich lists
bread = ['white', 'whole wheat']  # index positions: white = 0, whole wheat = 1
meat = ['chicken', 'salami', 'bacon', 'tuna'] # index: chicken = 0, salami = 1, bacon = 2, tuna = 3
veggie = ['lettuce', 'tomato', 'onions', 'pickles', 'peppers']


# message to users
print("Welcome to Random Sandwich Generator! We have the following selections: ")
print("Breads:", bread)  # print all the items in the list by entering the list name
print("Meat:", meat)
print("Veggies:", veggie)

#Ask user to press "Enter"
input("Press Enter to generate a random sandwich.") #dont need a variable because the user's input is not used else where in the code

selected_bread = random_selector(bread)
selected_meat = random_selector(meat)
selected_veggie = random_selector(veggie)

# message to users
print("Your random sandwich is:")
print(selected_meat, "and", selected_veggie, "on", selected_bread, "bread")
print("Enjoy!")
