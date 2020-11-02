# Beginner SEV - for loop number guessing game

import random

random_num = random.randint(1, 10)
chances = 3  # number of chances to guess the number

print("Your job is to guess the secret number.")
print("You will have", str(chances), "chances to guess.")

for i in range(chances):  # the for loop will run 3 times
    guess = input("Enter guess: ") # update cv
    if int(guess)  != random_num:
        print("You guessed wrong!")
    else:
        print("You won!")
        break

# once the for loop ends
print("The secret number was", str(random_num))

