#  A function is defined with switch statement in it.
def func(value):
    match value:
        case [11, 67, 95]:
            return 'pvdlz'
        case 'pvdlz':
            return [11, 67, 95]
        case _:
            return "default"


a = func([11, 67, 95])
b = func('pvdlz')
c = func(8.26)
