from random import randint
roll_dice == input(f'roll the dice? (y/n): ')

def diceroll():
    roll = randint(1, 7)
    return roll

def rollfunction():
    roll_dice == input(f'roll the dice? (y/n): ')
    while roll_dice == 'y':
        diceroll1 = diceroll()
        diceroll2 = diceroll()
        print(f'Dice roll 1: {diceroll1}')
        print(f'Dice roll 2: {diceroll2}')
        Total = diceroll1 + diceroll2
        print(f'total: {Total}')
        roll_dice == input(f'roll the dice? (y/n): ')
        if roll_dice == 'n':
            break


rollfunction()