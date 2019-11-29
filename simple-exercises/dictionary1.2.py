club = list()
player = dict()
goals = list()

while True:
    player.clear()
    player['name'] = str(input('Name: '))
    games = int(input('Number of games played: '))
    goals.clear()
    for c in range(0, games):
        goals.append(int(input(f'Goals on game {c}? ')))
    player['goals'] = goals[:]
    player['totalGoals'] = sum(goals)
    club.append(player.copy())
    while True:
        resp = str(input('You want to continue? [Y/N]'))[0]
        if resp.upper() in 'YN':
            break
        print('ERROR: Please answer Y or N')
    if resp.upper() == 'N':
        break
print('-='*20)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(club):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*20)

while True:
    code = int(input('Type a player code to see the details or 999 to stop: '))
    if code == 999:
        print('Bye! :)')
        break
    elif code >= len(club):
        print(f'ERROR: Code {code} does not exist!')
    else:
        print(f'SHOWING PLAYER "{club[code]["name"]}" INFORMATION')
        for index, goals in enumerate(club[code]['goals']):
            print(f'    On game {index+1} it scored {goals} goals.')
    print('-='*20)
