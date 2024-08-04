# The decorator is a function call.


def func1():
    def dec(f):
        return inner

    def inner():
        return 45.78

    return dec


@func1()
def func2():
    return [73, 70, 66]


a = func2()
