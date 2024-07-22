# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'ezrde': 7, 'hmfzu': 30, 'synez': 5}


def func2():
    return 11.71


def func3():
    return 10


def func4():
    return (12, 39, 84)


(a, b), (c, d) = [(func1, func2), (func3, func4)]
