import random
from words import words
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]

# Picking a word
word = random.choice(words)
print(word)

# Dashes
current_guess = "-" * len(word)
print(current_guess)

# Used Letters
letters_guessed = []

# Lives
lives = 0

while True:
    # Stores Guess in list
    print("Enter your guess here: ")
    letter = input()
    letters_guessed.append(letter)
    print(letters_guessed)

    # Checks for duplicates in the list

    if letter in letters_guessed:
        print("You have used this letter already")








        










