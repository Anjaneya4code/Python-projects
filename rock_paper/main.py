import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0


def get_winner(user, computer):
    if user == computer:
        return "draw"

    if (
        (user == "rock" and computer == "scissors")
        or
        (user == "paper" and computer == "rock")
        or
        (user == "scissors" and computer == "paper")
    ):
        return "user"

    return "computer"


def play_game():
    global user_score, computer_score

    print("\n===== ROCK PAPER SCISSORS =====")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice: ")

        if choice == "4":
            break

        if choice not in ["1", "2", "3"]:
            print("Invalid choice. Try again.")
            continue

        user_choice = choices[int(choice) - 1]
        computer_choice = random.choice(choices)

        print("\nYou chose:", user_choice)
        print("Computer chose:", computer_choice)

        winner = get_winner(user_choice, computer_choice)

        if winner == "user":
            print("🎉 You win!")
            user_score += 1

        elif winner == "computer":
            print("💻 Computer wins!")
            computer_score += 1

        else:
            print("🤝 It's a draw!")

        print(
            f"Score → You: {user_score} | "
            f"Computer: {computer_score}"
        )

    print("\n===== FINAL SCORE =====")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
    print("Thanks for playing!")


play_game()
