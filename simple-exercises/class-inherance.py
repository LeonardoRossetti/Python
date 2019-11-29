class Father:
    var1 = 'this is the class father'

    def showMessage(self, message):
        self.var1 = message
        print(self.var1)


class Child(Father):
    pass


Child().showMessage('Hey Anakin, I am your child!')
