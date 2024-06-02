# build a rock-paper-scissors-lizard-spock game which involves the user plays with the computer as its opponent.
# The winner is determined by the rules: rock beats scissors, scissors beats paper, paper beats rock, rock beats lizard, lizard beats spock, spock beats scissors, scissors beats lizard, lizard beats paper, paper beats spock, and spock beats rock.
# The program keeps track of the number of wins, losses, and ties.
# The user can play as many times as they want. The program will ask the user if they want to play again.
# The program will display the number of wins, losses, and ties at the end of each game.
# Prompts other than rock, paper, scissors will be considered invalid and the user will be asked to enter a valid input.

# Example: The user is asked to select either rock, paper, or scissors. The computer randomly selects one of the three options.
# Input : Rock
# Output: Computer selects Scissors
#         You win!


import random
choices = ["rock", "paper", "scissors", "lizard", "spock"]
wins = 0
losses = 0
ties = 0
rounds = 0

def play_game():
    global wins, losses, ties, rounds
    user_choice = input("\nEnter rock, paper, scissors, lizard or spock: ").lower()
    computer_choice = random.choice(choices)
    print(f"Computer selects {computer_choice}")

    rounds += 1
    if user_choice == computer_choice:
        print("It's a tie!")
        ties += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        wins += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        wins += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        wins += 1
    elif user_choice == "rock" and computer_choice == "lizard":
        print("You win!")
        wins += 1
    elif user_choice == "lizard" and computer_choice == "spock":
        print("You win!")
        wins += 1
    elif user_choice == "spock" and computer_choice == "scissors":
        print("You win!")
        wins += 1
    elif user_choice == "scissors" and computer_choice == "lizard":
        print("You win!")
        wins += 1
    elif user_choice == "lizard" and computer_choice == "paper":
        print("You win!")
        wins += 1
    elif user_choice == "paper" and computer_choice == "spock":
        print("You win!")
        wins += 1
    elif user_choice == "spock" and computer_choice == "rock":
        print("You win!")
        wins += 1
    elif user_choice not in choices:
        print("\nERROR: Invalid input. Please enter rock, paper, or scissors.\n")
    else:
        print("You lose!")
        losses += 1

def main():
    play_game()
    while True:
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again == "y":
            play_game()
        elif play_again == "n":
            print(f"\nYour Stats:\nTotal Rounds: {rounds}\nWins: {wins}\nLosses: {losses}\nTies: {ties}\n")
            print("Well played! See you later!")
            break
        else:
            print("\nERROR: Invalid input. Please enter y or n.\n")


if __name__ == "__main__":
    main()