from random import randint
from colorama import Fore, Style
from time import sleep

computerWonMessage = Fore.RED + 'COMPUTER WON!'
playerWonMessage = Fore.GREEN + 'PLAYER WON!'
gameTied = Fore.YELLOW + 'THE GAME TIED!'

options = ('Paper', 'Rock', 'Scissors')
computer = randint(0, 2)

try:
    for index, option in enumerate(options):
        print('[{}] {}'.format(index, option))

    userOption = int(input('Choose: '))

    if userOption < 0 or userOption > len(options) - 1:
        raise ValueError('Option [{}] is not valid.'.format(userOption))
except ValueError as e:
    print('Option invalid. {}'.format(e))
else:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')
    sleep(0.5)

    print('-=' * 10)
    print('Computer: {}'.format(options[computer]))
    print('Player: {}'.format(options[userOption]))
    print('-=' * 10)
    if userOption == computer:
        print(gameTied)
    elif userOption == 0 and computer == 1:
        print(playerWonMessage)
    elif userOption == 0 and computer == 2:
        print(computerWonMessage)
    elif userOption == 1 and computer == 0:
        print(computerWonMessage)
    elif userOption == 1 and computer == 2:
        print(playerWonMessage)
    elif userOption == 2 and computer == 0:
        print(playerWonMessage)
    elif userOption == 2 and computer == 1:
        print(computerWonMessage)
finally:
    print(Style.RESET_ALL)  # to reset the color settings
    del options  # delete the tuple from the memory
