# Method Overriding by imherited class
class MyClass:
    def func(self):
        return True


class MySubClass(MyClass):
    def func(self):
        return (2, 61, 88)


a = MySubClass()
b = a.func()
