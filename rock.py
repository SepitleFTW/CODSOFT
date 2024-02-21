import random
import time
from colorama import Fore, Style

choices = ["rock", "scissors", "paper"]  # player's choices
running = True

while running:
    player = None
    computer = random.choice(choices)

    # Reprompt the player if choice not available
    while player not in choices:
        player = input("Select your choice: ").lower()

    print("Rock...")
    time.sleep(0.5)
    print("Paper...")
    time.sleep(0.5)
    print("Scissors!")
    time.sleep(0.5)

    print(f"Player: {player.capitalize()}")
    print(f"Computer: {computer.capitalize()}")

    if player == computer:
        print(Fore.YELLOW + "It's a tie!")
    elif (player == "rock" and computer == "scissors") or (
        player == "scissors" and computer == "paper"
    ) or (player == "paper" and computer == "rock"):
        print(Fore.GREEN + "You Win!")
    else:
        print(Fore.RED + "You Lose!")

    print(Style.RESET_ALL)

    if input("Would you like to play again? (yes/no): ").lower() != "yes":
        running = False
