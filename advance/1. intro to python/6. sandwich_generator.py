# Advanced SEV and NEXUS - List Demo_________________________________________

from random import *

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

# generate a random index position
bread_size = len(bread) #get the size of the bread list
meat_size = len(meat) #get the size of the meat list
veggie_size = len(veggie)#get the size of the veggie list

bread_idx = randint(0, bread_size - 1)
meat_idx = randint(0, meat_size - 1)
veggie_idx = randint(0, veggie_size - 1)

# message to users
selected_bread = bread[bread_idx]
selected_meat = meat[meat_idx]
selected_veggie = veggie[veggie_idx]


print("Your random sandwich is:")
print(selected_meat, "and", selected_veggie, "on", selected_bread, "bread")
print("Enjoy!")
