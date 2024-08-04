# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 41


def func2():
    return [33, 42, 15]


def func3():
    return (99, 52, 66)


def func4():
    return 'vawmb'


(a, b), (c, d) = [(func1, func2), (func3, func4)]
