# Lists containing lists that contain functions.


def func1():
    return False


def func2():
    return 10.86


ls = [[func1], func2]

a = ls[0]
b = a[0]
c = b()
