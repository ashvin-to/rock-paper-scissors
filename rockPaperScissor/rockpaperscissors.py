print("Welcome to ROCK PAPER SCISSORS game!!")
import random
import re
import os


def check_play_status():
    valid_response = ['yes', 'y']
    while True:
        try:
            response = input("DO you want to continue: ")
            if response.lower() in valid_response:
                return True
            else:
                print('Thanks for playing!')
                exit()

        except ValueError as err:
            print(err)


def rps():
    play = True
    while play:
        print("Choose Rock, Paper, Scissors -Shoot!.")
        user_choice = input("Choose your response Rock[R], Scissors[S], Paper[P]:-")

        if not re.match("[SsRrPp]", user_choice):
            print('Please choose a letter:')
            print('[R]ock, [P]aper, or [S]cissors')
            continue

        print(f"You choose: {user_choice}")
        choices = ["R", "P", "S", "r", "p", "s"]
        computer_choice = random.choice(choices)
        print(f"I choose: {computer_choice}")

        if computer_choice == user_choice.upper():
            print('Tie!')
            play = check_play_status()
        elif computer_choice == 'R' and user_choice.upper() == 'S':
            print('Rock beats scissors, I win!')
            play = check_play_status()
        elif computer_choice == 'S' and user_choice.upper() == 'P':
            print('Scissors beats paper! I win!')
            play = check_play_status()
        elif computer_choice == 'P' and user_choice.upper() == 'R':
            print('Paper beats rock, I win!')
            play = check_play_status()
        else:
            print('You win!\n')
            play = check_play_status()


rps()
