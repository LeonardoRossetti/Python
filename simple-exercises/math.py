import math #to import the whole library
#from math import trunc, floor ceil #to import only the trunc function. (on this case, don't need to call math.trunc(...), just trunc(...))
num = float(input('Number: '))
print('The number is {} and the integer part is {}'.format(num, math.trunc(num)))
print('A raiz quadrada é: {}'.format(math.sqrt(num)))
print('A raiz quadrada é: {:.2f}'.format(math.sqrt(num))) #2 decimals
print('Ceil: {}'.format(math.ceil(num)))
print('Floor: {}'.format(math.floor(num)))

'''
print('acos: {}'.format(math.acos(num)))
print('acosh: {}'.format(math.acosh(num)))
print('asin: {}'.format(math.asin(num)))
print('atan: {}'.format(math.atan(num)))
print('atanh: {}'.format(math.atanh(num)))
print('copysign: {}'.format(math.copysign(num)))
'''
