class Car:
    # Private properties
    __name = ''
    __year = 0

    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    def getName(self):
        return self.__name

    def getYear(self):
        return self.__year


car = Car('Mustang', 2019)
print(car.getName())
print(car.getYear())
