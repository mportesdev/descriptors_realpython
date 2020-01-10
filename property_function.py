class Foo:
    def getter(self):
        print('Accessing the attribute to get the value')
        return 42

    def setter(self, value):
        print('Accessing the attribute to set the value')
        raise AttributeError('Cannot change the value')

    attribute1 = property(getter, setter)


my_foo_object = Foo()

x = my_foo_object.attribute1

print(x)
