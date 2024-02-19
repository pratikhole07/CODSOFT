import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_again():
    play_again = input("Do you want to play again? (yes/no): ")
    return play_again.lower() == 'yes'

user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors!")

while True:
    print("\nChoose one: rock, paper, scissors")
    user_choice = input("Your choice: ").lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("Your choice:", user_choice)
    print("Computer's choice:", computer_choice)

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    print("Your score:", user_score)
    print("Computer's score:", computer_score)

    if not play_again():
        break

print("Thank you for playing!")