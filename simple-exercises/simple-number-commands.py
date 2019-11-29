

while True:
    isNumeric = False
    number = str(input('Number > 0 and < 9999: '))
    if number.isnumeric():
        number = int(number)
        if 0 < number < 9999:
            break
    print(f'"{number}" is not a valid number between 0 and 9999. Try again.')

# number // 1 gets the integer part of division. E.g.: 5 // 2 = 2
u = number // 1 % 10
t = number // 10 % 10
h = number // 100 % 10
th = number // 1000 % 10
print('Unity {}, Ten {}, Hundred {}, Thousand {}'.format(u, t, h, th))

print('Number in binary is {}'.format(bin(number)[2:]))
print('Number in binary is {}'.format(bin(number)))
print('Number in octal is {}'.format(oct(number)[2:]))
print('Number in octal is {}'.format(oct(number)))
print('Number in hexadecimal is {}'.format(hex(number)[2:]))
print('Number in hexadecimal is {}'.format(hex(number)))

