import random
# developed by Prajwal Nivangune
def get_user_choice():
    '''Get the user's choice (rock, paper, or scissors)'''
    while True:
        try:
            user_choice = input("choose rock, paper, scissors :").lower()
            if user_choice in ['rock','paper','scissors']:
                return user_choice
            else:
                raise ValueError("Invalid Choice! Please enter rock, paper, or scissors.")
        except ValueError as e:
            return e

def get_computer_choice():
    '''Get the computer choice by using random library'''
    return random.choice(['rock','paper','scissors'])

def games_logic(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper')):
        return "Congrats, You Win!"
    else:
        return "You Lose!"


def play_game():
    print("Let's Play rock paper scissors :) ")
    user_score = 0
    computer_score = 0
    while True:
        try:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print(f"You chose {user_choice}.")
            print(f"The computer chose {computer_choice}.")

            result = games_logic(user_choice,computer_choice)
            print(result)
            if "Win" in result:
                user_score += 1
            elif "Lose" in result:
                computer_score += 1

            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing! Final Scores:")
                print(f"User Score: {user_score} | Computer Score: {computer_score}")
                break


        except KeyboardInterrupt:
            print("\nGame aborted. Goodbye!")
            return


if __name__ == "__main__":
    play_game()