# Lists containing lists that contain functions.


def func1():
    return 'kfyjo'


def func2():
    return False


ls = [[func1], func2]

a = ls[0]
b = a[0]
c = b()
