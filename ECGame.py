import random

# Write the function to randomly select the computer's choice
def get_computer_choice():
    choices = ['r', 'p', 's']  # Possible choices: Rock (R), Paper (P), Scissors (S)
    return random.choice(choices)  # Randomly select one of the choices

# Write the function to determine the winner of the game based on player and computer choices
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"  # Both player and computer choose the same option
    elif (player_choice == 'r' and computer_choice == 's') or \
            (player_choice == 'p' and computer_choice == 'r') or \
            (player_choice == 's' and computer_choice == 'p'):
        return "player"  # Player wins
    else:
        return "computer"  # Computer wins

def main():
    player_score = 0  # Initialize player's score
    computer_score = 0  # Initialize computer's score

    while True:  # Main game loop
        player_choice = input("Enter a choice (Rock(r), Paper(p), Scissors(s)): ").lower()

        # Validate player input
        if player_choice not in ['r', 'p', 's']:
            print("I didn't get it! Please enter 'r', 'p', or 's'.")
            continue  # Prompt for input again if invalid

        computer_choice = get_computer_choice()  # Get computer's choice

        print(f"\nYou chose {player_choice}, the computer chose {computer_choice}.")  # Display choices

        winner = determine_winner(player_choice, computer_choice)  # Determine the winner

        # Output the result of the round
        if winner == "tie":
            print(f"Both players selected {player_choice}. It's a tie!")
        elif winner == "player":
            print(f"{player_choice.upper()} beats {computer_choice.upper()}! You win!")
            player_score += 1  # Increment player score
        else:
            print(f"{computer_choice.upper()} beats {player_choice.upper()}! You lose!")
            computer_score += 1  # Increment computer score

        play_again = input("Play again? (y/n): ").lower()  # Ask if the player wants to play again
        if play_again != 'y':
            print("Goodbye!")  # Print goodbye message
            break  # Leave the game - and the loop

    # Print final scores after the game ends
    print("\nFinal Scores:")
    print(f"Computer: {computer_score}")
    print(f"Player: {player_score}")

# Entry point for the program
if __name__ == "__main__":
    main()