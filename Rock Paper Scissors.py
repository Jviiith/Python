import random


def play():
    user = input(
        "Pick Your Poison -> 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    if winner(user, computer):
        return 'You won'
    return 'You lost'


def winner(player, opponent):
    # return true if player wins
    # winnning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
