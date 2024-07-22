# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return 'disqu'


def func2():
    return 45.14


def func3():
    return (51, 90, 7)


def func4():
    return [96, 92, 33]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
