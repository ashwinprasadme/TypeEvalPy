# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return 'qzfzn'

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return (42, 51, 39)


a = MyClass()
b = a.my_method()
