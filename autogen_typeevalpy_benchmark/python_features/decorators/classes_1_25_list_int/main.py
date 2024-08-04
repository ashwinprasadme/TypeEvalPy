# Class with a decorator.


def my_decorator(cls):
    class NewClass(cls):
        def my_method(self):
            return [60, 11, 12]

    return NewClass


@my_decorator
class MyClass:
    def my_method(self):
        return 57


a = MyClass()
b = a.my_method()
