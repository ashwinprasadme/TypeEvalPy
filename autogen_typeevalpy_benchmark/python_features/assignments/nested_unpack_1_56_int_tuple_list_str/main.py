# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 95


def func2():
    return (82, 4, 12)


def func3():
    return [96, 68, 28]


def func4():
    return 'jleii'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
