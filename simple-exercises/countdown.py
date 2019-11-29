from time import sleep

#for c in range(0, 5):
#    print(c)

#for c in range(5, 0, -1): #(from, to, 1 by 1)
#    print(c)

try:
    number = int(input('Type a number: '))
    if number < 0:
        raise ValueError('Only numbers bigger than zero are allowed!')
except ValueError as e:
    print('Error: {}'.format(e))
else:
    for n in range(number, 0, -1):
        print(n)
        sleep(1)
finally:
    print('END!')
