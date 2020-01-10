class VerboseAttribute:
    def __get__(self, obj, type=None):
        print('Accessing the attribute to get the value')
        return 42

    def __set__(self, obj, value):
        print('Accessing the attribute to set the value')
        raise AttributeError('Cannot change the value')


class Foo:
    attribute1 = VerboseAttribute()


my_foo_object = Foo()

x = my_foo_object.attribute1

print(x)
