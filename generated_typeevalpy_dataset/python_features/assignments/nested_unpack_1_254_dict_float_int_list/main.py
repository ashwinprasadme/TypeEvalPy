# example of nested unpacking in Python. The list [(func1, func2), (func3, func4)] contains two tuples, each with two function objects.
# The outer parentheses in the assignment (a, b), (c, d) = ... are used for nested unpacking.


def func1():
    return {'chqbt': 19, 'cqyzj': 66, 'vimez': 52}


def func2():
    return 70.66


def func3():
    return 21


def func4():
    return [69, 15, 65]


(a, b), (c, d) = [(func1, func2), (func3, func4)]
