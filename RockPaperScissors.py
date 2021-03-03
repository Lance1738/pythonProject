import random

while True:

    def rps():
        user = input("Rock Paper Scissors: ")
        answers = ["Rock", "Paper", "Scissors"]
        choice = random.choice(answers)

        # Output for Rock
        if user == "r" and choice == "Rock":
            print("The computer chose " + choice + ". It's a Tie.")

        elif user == "r" and choice == "Paper":
            print("The computer chose " + choice + ". You Lose.")

        elif user == "r" and choice == "Scissors":
            print("The computer chose " + choice + ". You Win.")

        # Output for Paper

        elif user == "p" and choice == "Scissors":
            print("The computer chose " + choice + ". You Lose.")

        elif user == "p" and choice == "Rock":
            print("The computer chose " + choice + ".  You Win.")

        elif user == "p" and choice == "Paper":
            print("The computer chose " + choice + ". It's a tie.")

        # Output for Scissors

        elif user == "s" and choice == "Rock":
            print("The computer chose " + choice + ". You Lose.")

        elif user == "s" and choice == "Paper":
            print("The computer chose " + choice + ". You Win.")

        elif user == "s" and choice == "Scissors":
            print("The computer chose " + choice + ". It's a tie.")
        else:
            print("Invalid")
    rps()
