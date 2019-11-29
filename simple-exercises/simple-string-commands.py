#https://docs.python.org/3/library/stdtypes.html#truth-value-testing


name = str(input('Type your full name: ')).strip()  # .strip() func works like a Trim() in C#

if not name:
    print('Please enter a valid name.')
else:
    print('Your name contains {} letters'.format(len(name) - name.count(' ')))  # doesn't count spaces in between
    print('Uppercase: {}'.format(name.upper()))
    print('Lowercase: {}'.format(name.lower()))

    splitWords = name.split(' ')
    print(splitWords)
    print('First name is {} and it contains {} letters'.format(splitWords[0], len(splitWords[0])))
    print('Last name is {} and it contains {} letters'.format(splitWords[len(splitWords)-1], len(splitWords[len(splitWords)-1])))

    print('Name contains "Leo": {}'.format('leo' in name.lower()))

    print('Letter "A" appears {} times.'.format(name.lower().count('a')))

    print('The first letter "A" was on position {}'.format((name.lower().find('a'))))
    print('The last letter "A" was on position {}'.format((name.lower().rfind('a')))) #start from the right

    message = 'abcdefghijkl'
    print(message[2:])


