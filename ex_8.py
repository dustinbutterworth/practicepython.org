#!/usr/bin/env python3
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def winner(player1_choice,player2_choice):
    player1_win_message = 'Player 1 wins!'
    player2_win_message = 'Player 2 wins!'
    tie_message = 'Players tied!'
    if player1_choice == player2_choice:
        return tie_message
    elif player1_choice == 'rock':
        if player2_choice == 'scissors':
            return player1_win_message
        else:
            return player2_win_message
    elif player1_choice == 'paper':
        if player2_choice == 'rock':
            return player1_win_message
        else:
            return player2_win_message
    elif player1_choice == 'scissors':
        if player2_choice == 'paper':
            return player1_win_message
        else:
            return player2_win_message


def main():
    choices = ['rock', 'paper', 'scissors']
    while True:
        player1_choice = str(input("Player 1, choose rock, paper, or scissors:\n"))
        if player1_choice not in choices:
            print(f'{player1_choice} is not rock, paper, or scissors')
            continue
        else:
            break
    while True:
        player2_choice = str(input("Player 2, choose rock, paper, or scissors:\n"))
        if player2_choice not in choices:
            print(f'{player2_choice} is not rock, paper, or scissors')
            continue
        else:
            break
    print(f'Player 1 chose {player1_choice}')
    print(f'Player 2 chose {player2_choice}')
    print(winner(player1_choice,player2_choice))

if __name__ == '__main__':
    main()