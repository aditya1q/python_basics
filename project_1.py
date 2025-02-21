import random

computer = random.choice([1, 0, -1])
you_str = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ")
you_dict = {"r": 1, "p": -1, "s": 0}
reverse_dict = {1: "Rock", -1: "Paper", 0: "Scissors"}

if you_str not in you_dict:
    print("Invalid choice! Please enter 'r', 'p', or 's'.")
else:
    your_choice = you_dict[you_str]
    
    print(f"You chose {reverse_dict[your_choice]}")
    print(f"Computer chose {reverse_dict[computer]}")
    
    if your_choice == computer:
        print("Match Draw")
    elif (your_choice == 1 and computer == -1) or (your_choice == -1 and computer == 0) or (your_choice == 0 and computer == 1):
        print("You win!")
    else:
        print("You lose!")