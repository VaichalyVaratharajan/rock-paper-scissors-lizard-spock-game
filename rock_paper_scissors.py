import random

def game():
    print("================================")
    print("Rock Paper Scissors Lizard Spock")
    print("================================")
    
    for i in range(100):
        print("1) ✊")
        print("2) ✋")
        print("3) ✌️")
        print("4) 🦎")
        print("5) 🖖")
        print("6) Quit")
        
        player = int(input("Pick a number: "))
        if player == 6:
            print("Thanks for playing!")
            break
        elif player >= 1 and player <= 5:
            show_player_choice(player)
        else:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        
        if player == computer_choice:
            print("It's a tie!")
        elif (player == 1 and computer_choice == 3) or \
             (player == 1 and computer_choice == 4) or \
             (player == 2 and computer_choice == 1) or \
             (player == 2 and computer_choice == 5) or \
             (player == 3 and computer_choice == 2) or \
             (player == 3 and computer_choice == 4) or \
             (player == 4 and computer_choice == 5) or \
             (player == 4 and computer_choice == 2) or \
             (player == 5 and computer_choice == 1) or \
             (player == 5 and computer_choice == 3):
            print("You win!")
        else:
            print("Computer wins!")
        
        user_input = input("Do you want to play again? (yes/no): ")
        if user_input.lower() != "yes":
            break
        else:
            print("Let's play again!")
            print()

def show_player_choice(choice):
    if choice == 1:
        print("You chose: ✊")
    elif choice == 2:
        print("You chose: ✋")
    elif choice == 3:
        print("You chose: ✌️")
    elif choice == 4:
        print("You chose: 🦎")
    elif choice == 5:
        print("You chose: 🖖")

def get_computer_choice():
    computer_choice = random.randint(1, 5)  # Fixed to include all 5 options
    if computer_choice == 1:
        print("CPU chose: ✊")
    elif computer_choice == 2:
        print("CPU chose: ✋")
    elif computer_choice == 3:
        print("CPU chose: ✌️")
    elif computer_choice == 4:
        print("CPU chose: 🦎")
    elif computer_choice == 5:
        print("CPU chose: 🖖")
    
    return computer_choice

if __name__ == "__main__":
    game()