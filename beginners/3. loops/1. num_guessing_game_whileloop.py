# Beginner SEV - while loop number guessing game

import random

random_num = random.randint(1, 10)

print("Your job is to guess the secret number.")
guess = input("Enter guess: ")  # first intialize the cv

while int(guess) != random_num:
	print("You guessed wrong")  # statement to user
	guess = input("Enter guess: ")  # update cv

# once the loop ends
print("You win! The secret number was", random_num)
