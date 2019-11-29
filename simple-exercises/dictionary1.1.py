from datetime import datetime

data = dict()

data['Name'] = str(input('Name: '))
data['Born'] = int(input('Year you were born: '))
data['Age'] = datetime.now().year - data['Born']
isWorking = str(input('Is working(y/n) '))
if isWorking == 'y':
    data['startedWorkingOn'] = int(input('Year that you started working: '))
    data['RetireAge'] = data['Age'] + ((data['startedWorkingOn'] + 35) - datetime.now().year)

for k, v in data.items():
    print(f'{k}: {v}')
