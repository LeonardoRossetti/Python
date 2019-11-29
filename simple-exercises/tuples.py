from random import randint
# IMPORTANT: Tuples are immutable. However, we can delete a Tuple from memory using: del(tuple)
#            Tuples can accept different data. E.g. ('Leo', 25, 'M', 72.10)

heroes = ('Wonder Woman', 'Spider Man', 'Batman', 'Iron Man')
realNames = 'Diana Prince', 'Peter Parker', 'Bruce Wayne', 'Tony Stark'  # it is also a tuple
mix = heroes + realNames

print('-=' * 20)
print('READING')
print('-' * 20)
for hero in heroes:
    print(hero)

for cont in range(0, len(mix)):
    print(mix[cont])

for pos, name in enumerate(mix):
    print(f'I would like to see {name} on position {pos}.')  # Python 3.6+

print(f'First five names are {mix[0:5]}')
print(f'Last five names are {mix[-5:]}')


print('\n\n', end='-=' * 20)
print('\nSearching for letters into words')
print('-' * 20)
for hero in heroes:
    print(f'\nOn the name {hero} we have ', end='')
    for letter in hero:
        if letter.lower() in 'aeiou':
            print(f'{letter}', end=' ')

print('\n\n', end='-=' * 20)
print('\nSorting')
print('-' * 20)
print(sorted(mix))  # It becomes a list when sorting

print('\n\n', end='-=' * 20)
print('\nFinding the index')
print('-' * 20)
print(mix.index('Batman'))
print(mix.index('Batman', 2))  # Start searching on position 2

for hero, name in zip(heroes, realNames):
    print(f'{hero :.<30} is actually ', end='')
    print(f'{name:>5.15}')


numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('The sorted numbers are: ', end='')
for n in numbers:
    print(f'{n} ', end='')
print(f'\nThe biggest value is {max(numbers)}')
print(f'The smallest value is {min(numbers)}')
if 9 in numbers:
    print(f'The value 9 appeared {numbers.count(9)} times. The first one was on position {numbers.index(9)}')
else:
    print('The value 9 does not appear in the tuple')
