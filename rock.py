# a simple rock, paper and scissors game

import random

choices = ["rock", "scissor", "paper"] #players choices
running = True

while running:

    player = None
    computer = random.choice(choices)

    #reprompt the player if choice not available
    while player not in choices:
        player = input("Select your choice:")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Tie!")

    elif player == "rock" and computer == "scissors":
        print("You Win!")

    elif player == "paper" and computer == "rock":
        print("You Win!")

    elif player == "scissors" and computer == "paper":
        print("You Win!")

    else:
        print("You Lose!")

    if not input("Would you like to play again? (yes/no):").lower() == "yes":
        running = Fale  


