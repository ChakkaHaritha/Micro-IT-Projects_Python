import random

print("=== Rock Paper Scissors Game ===")
print("Choose one among the options: rock, paper, scissors")

user_choice = input("Enter your choice: ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"\nYou chose: {user_choice}")
print(f"Computer chose: {computer_choice}\n")

if user_choice == "rock":
    if computer_choice == "rock":
        print("It's a tie!")
    elif computer_choice == "paper":
        print("Computer wins!")
    elif computer_choice == "scissors":
        print("You win!")
    else:
        print("Invalid computer choice!")

elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    elif computer_choice == "paper":
        print("It's a tie!")
    elif computer_choice == "scissors":
        print("Computer wins!")
    else:
        print("Invalid computer choice!")

elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Computer wins!")
    elif computer_choice == "paper":
        print("You win!")
    elif computer_choice == "scissors":
        print("It's a tie!")
    else:
        print("Invalid computer choice!")

else:
    print("Invalid input. Please choose rock, paper, or scissors.")
