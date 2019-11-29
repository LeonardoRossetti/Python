#  Lists are mutable
#  To include new items in a list: myList.appent
#  To remove items from a list: myList.pop(index)  or  myList.remove('item')  or del myList[index]
#  myList.pop() will remove the last item of the list

numbers = [0, 2, 3, 5]
numbers[0] = 1
numbers.insert(3, 4)  # (position, value)
numbers.append(6)
print(f'append(6) -> {numbers}')
numbers.sort(reverse=True)
print(f'sort(reverse=True) -> {numbers}')
numbers.pop()
print(f'Pop() -> {numbers}')
numbers.pop(4)
print(f'Pop(4) -> {numbers}')
numbers.append(3)
print(f'append(3) -> {numbers}')
if 3 in numbers:  # important to always be sure that the item is in the list before remove it
    numbers.remove(3)
    print(f'remove(3) -> {numbers}')  # remove the first occurrence only
newNumbers = numbers
newNumbers[0] = 10  # it changed both lists, because they have the same data reference
print(f'numbers -> {numbers}')
print(f'newNumbers -> {newNumbers}')
copyNumbers = numbers[:]  # here we are creating a new data reference
copyNumbers[0] = 100
print(f'numbers -> {numbers}')
print(f'copyNumbers -> {copyNumbers}')
print(f'numbers[-1] -> {numbers[-1]}')  # get the last item of a list

