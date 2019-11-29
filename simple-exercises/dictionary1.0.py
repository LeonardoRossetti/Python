from random import randint
from operator import itemgetter

game = {'Player 1': randint(1, 6),
        'Player 2': randint(1, 6),
        'Player 3': randint(1, 6),
        'Player 4': randint(1, 6)}

for k, v in game.items():
    print(f'{k} played the number {v}')

print('-='*20)
print('  === RANKING ===')

gameSorted = list()
gameSorted = sorted(game.items(), key=itemgetter(1), reverse=True)

for index, value in enumerate(gameSorted):
    print(f'On position {index+1} is {value[0]} that played the number {value[1]}')

