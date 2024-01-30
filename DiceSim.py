# import random
# def a function to roll the dice
# create a dictionary that will contain drawings of the dice
# create a while loop to keep rolling a dice

import random


def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),

    }
    roll = input('Roll the dice (Y/N): '.lower())

    while roll == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print(f'Dice rolled: {dice1} and {dice2}')
        print('\n'.join(dice_drawing[dice1]))
        print('\n'.join(dice_drawing[dice2]))

        roll = input('Roll again (Y/N): '.lower())
    else:
        print('')
        print('Exit Dice roller')
        quit()


roll_dice()
