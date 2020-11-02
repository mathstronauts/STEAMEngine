# Advanced SEV - word guessing game - For Loop TEMPLATE

import mathstropy
import random

random_word = mathstropy.randomword()  # random word generator function
chances = 3  # number of trys to guess the number
hint = mathstropy.wordmask(random_word)

print("Your job is to guess the secret word.")
print("You will have", str(chances), "chances to guess.")

print(hint)

# create for loop

   
# once for loop is completed
print("The secret word was", random_word)

