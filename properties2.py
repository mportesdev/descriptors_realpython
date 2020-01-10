class EvenNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)


class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()


my_values = Values()

my_values.value1 = 1
my_values.value2 = 4

print(my_values.value1)
print(my_values.value2)
