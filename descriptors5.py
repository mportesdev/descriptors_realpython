class OneDigitNumericValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError('The value is invalid')
        obj.__dict__[self.name] = value


class Foo:
    number = OneDigitNumericValue()


my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)
