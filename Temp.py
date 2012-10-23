def bind(func, *param1):
    def f1(*args):
        return func(param1 + args)
    return f1


def my_func(*args):
    return
