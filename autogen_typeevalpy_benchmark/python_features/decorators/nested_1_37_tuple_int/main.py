# A function defined inside another function's context serves as a decorator.


def func():
    def dec(f):
        return modified_inner

    def modified_inner():
        return (30, 3, 85)

    @dec
    def inner():
        return 32

    return inner()


a = func()
