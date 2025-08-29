
"""
Rock-Paper-Scissors CLI game.
- Play rounds against the computer
- Tracks score for the session
- Type 'quit' to stop playing
"""

import random

CHOICES = ["rock", "paper", "scissors"]

WIN_MAP = {
    ("rock", "scissors"),
    ("scissors", "paper"),
    ("paper", "rock"),
}

def get_computer_choice():
    return random.choice(CHOICES)

def decide(user, comp):
    if user == comp:
        return "tie"
    if (user, comp) in WIN_MAP:
        return "user"
    return "computer"

def main():
    user_score = 0
    comp_score = 0
    rounds = 0
    print("Rock-Paper-Scissors! Type 'quit' to exit.")
    while True:
        user = input("Your choice (rock/paper/scissors): ").strip().lower()
        if user in ("quit", "exit"):
            break
        if user not in CHOICES:
            print("Invalid choice. Try again.")
            continue
        comp = get_computer_choice()
        result = decide(user, comp)
        rounds += 1
        if result == "tie":
            print(f"Both chose {user}. It's a tie.")
        elif result == "user":
            user_score += 1
            print(f"You chose {user}, computer chose {comp}. You win this round!")
        else:
            comp_score += 1
            print(f"You chose {user}, computer chose {comp}. Computer wins this round.")
        print(f"Score -> You: {user_score} | Computer: {comp_score} | Rounds: {rounds}\n")

    print("\nFinal score:")
    print(f"You: {user_score} | Computer: {comp_score} | Rounds: {rounds}")
    if user_score > comp_score:
        print("Overall winner: You! 🎉")
    elif comp_score > user_score:
        print("Overall winner: Computer. Try again!")
    else:
        print("Overall result: Tie.")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()

