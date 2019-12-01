class Person(object):
    def __init__(self, name):
        self.name = name

    def revealIdentity(self):
        print(f'My name is {self.name}')


class SuperHero(Person):
    def __init__(self, name, heroName):
        super(SuperHero, self).__init__(name)
        self.heroName = heroName

    def revealIdentity(self):  # overriding the function
        super(SuperHero, self).revealIdentity()
        print(f'... And I am {self.heroName}')


leo = Person('Leo')
leo.revealIdentity()

peterParker = SuperHero('Peter Parker', 'Spider Man')
peterParker.revealIdentity()
