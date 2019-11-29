import utils.mesage


# REMEMBER: Variables created into functions have a local scope only

def countAll(*numbers):  # * numbers means all possible numbers, we don't know exactly how many. A tuple will be created
    print(f'Numbers: {numbers}')
    return sum(numbers)


# Two rows between the functions
utils.mesage.showMessage('Starting...', '~')

print(countAll(1, 2, 3.3, 4, 5))

help(utils.mesage.showMessage)  # we can call helps for all functions on Python (e.g.: help(input), help(print)).
