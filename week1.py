import random
# This is the main game file that contains the main function to run the game.
# The import here is used to fetch or extract functions to perform random operations from the library.

def user_choice():
    # This function is used to get the user's choice of game.
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def computer_choice():
    # This function is used to get the computer's choice of game.
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user, computer):
    # This function is used to determine the winner of the game.
    if user == computer:
        return "It's a draw!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Main program flow
user = user_choice()
print("You selected:", user)

computer = computer_choice()
print("Computer selected:", computer)

result = determine_winner(user, computer)
print(result)
# This is the end of the game file.
# The game is a simple rock-paper-scissors game where the user plays against the computer.
# The user is prompted to enter their choices, and the computer randomly selects its choice from the same set of options.
# The winner is determined bassed on the rules of the game.
# The game continues until the user decides to stop playing or the computer wins.
