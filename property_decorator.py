class Foo:
    @property
    def attribute1(self):
        print('Accessing the attribute to get the value')
        return 42

    @attribute1.setter
    def attribute1(self, value):
        print('Accessing the attribute to set the value')
        raise AttributeError('Cannot change the value')


my_foo_object = Foo()

x = my_foo_object.attribute1

print(x)
