from datetime import date

try:
    year = int(input('Type an year or 0 to see current year: '))
    if year == 0:
        year = date.today().year
    if year < 0:
        raise ValueError('Negative numbers are not valid years.')
    isLeapYear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
except ValueError as e:
    print('Please, type only valid years. {}'.format(e))
else:
    print('The year {} '.format(year), end='')
    print('is a leap year' if isLeapYear else 'is not a leap year')
