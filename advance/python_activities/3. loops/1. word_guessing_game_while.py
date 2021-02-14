# Advanced SEV - word guessing game - While Loop

import mathstropy

random_word = mathstropy.randomword()  # random word generator function

print("Your job is to guess the secret word.")

hint = mathstropy.wordmask(random_word)
print(hint)  # this shows the masked word, some letters of the word are hidden

guess = input("Enter guess: ")  # initialize the cv

while guess.lower() != random_word.lower():  # while guess is not equal to the random word
    print("Sorry, guess incorrect.")
    guess = input("Enter guess: ")  # update the cv


# once while loop ends
print("You won! The secret word was", random_word)
