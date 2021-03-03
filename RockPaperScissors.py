import random

while True:

    def rps():
        user = input("Rock Paper Scissors: ")
        answers = ["Rock", "Paper", "Scissors"]
        choice = random.choice(answers)
        print(choice)

        if user == "r" and choice == "Rock":
            print("Tie")

        elif user == "r" and choice == "Paper":
            print("You Lose")

        elif user == "r" and choice == "Scissors":
            print("You Win")

        elif user == "p" and choice == "Scissors":
            print("You Lose")

        elif user == "p" and choice == "Rock":
            print("You Win")

        elif user == "p" and choice == "Paper":
            print("Tie")

        elif user == "s" and choice == "Rock":
            print("You Lose")

        elif user == "s" and choice == "Paper":
            print("You Win")

        elif user == "s" and choice == "Scissors":
            print("Tie")
        else:
            print("Invalid")
    rps()
