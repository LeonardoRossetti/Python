from random import randint
from colorama import Fore, Style
draw = randint(0, 5)
useHelp = True #It could be an input

print('-=-' * 20)
print("I'm thinking in a number between 0 and 5. Try to guess it... ")
pair = bool(draw % 2 == 0)

if useHelp:
    helpMessage = 'HELP: The number is'
    helpMessage += ' a pair' if pair else ' an odd'
    print(helpMessage)

print('-=-' * 20)

try:
    while True:
        playerGuess = int(input('Your guess is? '))
        if playerGuess > 5 or playerGuess < 0:
            print('Only numbers between 0 and 5 are valid.')
        #print(Fore.GREEN + 'You won!' if playerGuess == draw else Fore.RED + 'You lose!')
        if playerGuess == draw:
            print(Fore.GREEN + 'You won!')
            break
        else:
            print(Fore.RED + 'Try again!')
except ValueError as e:
    print('Only numbers are accepted! {}'.format(e))
finally:
    print(Style.RESET_ALL) #to reset the color settings

