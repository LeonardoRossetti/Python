find = 'd'
stack = ['a', 'b', 'c', 'd']

for letter in stack:
    if letter == find:
        print('Found!')
        break
else:  # If no break occurred
    print('Not found!')