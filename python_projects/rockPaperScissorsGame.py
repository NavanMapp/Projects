import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!!!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Computer wins!")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ", player)
            print("Player Wins!")
    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Player Wins!")
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer Wins!")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("Player wins!")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ", player)
            print("Computer Wins!")
    playAgain = input("Would you like to play again? (yes/no)").lower()

    if playAgain != "yes":
        break
print("Bye!")