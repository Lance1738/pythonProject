import random


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print("Welcome to the password generator. Please enter the number of characters you want your password to be.")
while True:

    try:
        guess = int(input("\nNumber of characters: "))

        for i in range(int(guess)):
            print(random.choice(letters), end='',)

    except:
        print("Invalid Input. Please enter an integer")














