# Beginner SEV - while loop number guessing game

import random

random_num = random.randint(1, 10)

print("Your job is to guess the secret number.")
guess = input("Enter guess: ")  # first intialize the cv

while int(guess) != random_num:
    if int(guess) > random_num:
        print("You guessed too high")  # statement to user
    elif int(guess) < random_num:
        print("You guessed too low")  # statement to user

    guess = input("Enter guess: ")  # update cv


# once the loop ends
print("You win! The secret number was", str(random_num))
