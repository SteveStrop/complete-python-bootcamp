class Super:
    def __init__(self):
        self.name = None

    def get_name(self):
        if self.name is None:
            self.name=input('Name please')

class Sub (Super):
    def __init__(self,super_class):
        Super.__init__(super_class)
        self.surname = 'Williams'

dummy = Super()
dummy.get_name()
test = Sub(dummy)

print(f'test stuff is : {test.name} {test.surname}')
print(f'dummy stuff is {dummy.name}')