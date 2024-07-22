# A function `func` is called and returns a function `return_func` which is later called directly in the form func()().


def return_func():
    def nested_return_func():
        return {'newhv': 41, 'iwygc': 27, 'thwfn': 69}

    return nested_return_func


def func():
    return return_func


a = func()()
b = func()()()
