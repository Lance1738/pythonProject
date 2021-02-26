word = "computer"
userguess = ""
lives = 10

while userguess != word:
    userguess = input("Enter Guess: ")

    if userguess != word:
        lives = lives - 1
        print("You have " + str(lives) + " lives left.")

    if lives == 0:
        print("You lose!")
        break

if userguess == word:
    print("You got it!")
