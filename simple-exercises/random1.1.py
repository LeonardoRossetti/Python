from random import choice, shuffle

name1 = str(input('Name 1:'))
name2 = str(input('Name 2:'))
name3 = str(input('Name 3:'))
myList = [name1, name2, name3]

#Choice
print('The chosen one is: {}'.format(choice(myList)))

#Shuffle
shuffle(myList)
print('Shuffle: {}'.format(myList))

