# Advanced SEV - word guessing game - For Loop TEMPLATE

import mathstropy

random_word = mathstropy.randomword()  # random word generator function
chances = 3  # number of trys to guess the number
hint = mathstropy.wordmask(random_word)

print("Your job is to guess the secret word.")
print("You will have", str(chances), "chances to guess.")

print(hint)

for i in range(chances):  # the for loop will run 3 times, the upper limit is one above the highest number we want to count to
    guess = input("Enter guess: ")
    
    if guess.lower() != random_word:
        print("Sorry, guess incorrect.")
    else:
        print("You won!")
        break

# once for loop is completed
print("The secret word was", random_word)
