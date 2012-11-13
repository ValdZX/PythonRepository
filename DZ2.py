def mul2(x):
    return x * 2


def is_positive(num):
    return num >= 0


def mul(a, b):
    return a * b


def inc(*args):
    rez = []
    for i in args:
        rez.append(i + 1)
    return rez


def func_math_asorty(a, b, c, d, e, f):
    rez = (a ** b) / (c * d) + (e - f)
    return rez


def f(a, b, c):
    return [a, b, c]


def map_rek(func, iter):
    rez = []
    if len(iter) > 0:
        rez.append(func(iter[0]))
        if len(iter) > 1:
            rez += map_rek(func, iter[1:])
    return rez


def filter_rek(func, arr):
    rez = []
    if len(arr) > 0:
        if func(arr[0]):
            rez.append(arr[0])
        if len(arr) > 1:
            rez += filter_rek(func, arr[1:])
    return rez


def reduse_rek(func, arr):
    assert len(arr) > 0
    elem = arr[0]
    if len(arr) > 1:
        elem = func(elem, reduse_rek(func, arr[1:]))
    return elem


def bind(func, *param1):
    def f1(*param2):
        return func(*(param1 + param2))
    return f1


def bind2(func, *param1, **name_param1):
    def f1(*param2, **name_param2):
        name_param1.update(name_param2)
        return func(*(param1 + param2), **name_param1)
    return f1


def bind3(func, *param1):
    if func.func_code.co_argcount > len(param1):
        def f1(*param2):
            if func.func_code.co_argcount > len(param1 + param2):
                return bind3(func, *(param1 + param2))
            elif func.func_code.co_argcount < len(param1 + param2):
                return f(*(param1 + param2)[0:func.func_code.co_argcount])
            else:
                return func(*(param1 + param2))
        return f1
    elif func.func_code.co_argcount < len(param1):
        return f(*param1[0:func.func_code.co_argcount])
    else:
        return f(*param1)


def test_map_rek():
    assert map_rek(mul2, (1, 2, 3)) == [2, 4, 6]
    assert map_rek(str, (1, 2, 3)) == ["1", "2", "3"]
    print "Test map_rek passed OK!"


def test_filter_rek():
    assert filter_rek(is_positive, []) == filter(is_positive, [])
    assert filter_rek(is_positive, [3, 0, 5, 7, 8, 1]) == filter(is_positive, [3, 0, 5, 7, 8, 1])
    assert filter_rek(is_positive, [-3, -2, -5, -7, -8, -1]) == filter(is_positive, [-3, -2, -5, -7, -8, -1])
    assert filter_rek(is_positive, [-3, 0, 5, -7, 8, -1]) == filter(is_positive, [-3, 0, 5, -7, 8, -1])
    print "Test filter_rek passed Ok!"


def test_my_reduse():
    assert reduse_rek(mul, [4]) == reduce(mul, [4])
    assert reduse_rek(mul, [2, 3]) == reduce(mul, [2, 3])
    assert reduse_rek(mul, [1, 2, 3, 4, 5]) == 2 * 3 * 4 * 5
    assert reduse_rek(mul, [0, 3, 4]) == reduce(mul, [0, 3, 4])
    assert reduse_rek(mul, [-2, -3, 9]) == reduce(mul, [-2, -3, 9])
    #assert reduse_rek(mul, []) == reduce(mul, [])
    print "Test reduse_rek passed Ok!"


def test_bind():
    f1 = bind(inc, 0, 2, 4, 6)
    assert f1(1, 3, 5) == [1, 3, 5, 7, 2, 4, 6]
    f1 = bind(inc)
    assert f1(1, 3, 5) == [2, 4, 6]
    f1 = bind(inc, 0, 2, 4, 6)
    assert f1() == [1, 3, 5, 7]
    print "Test bind passed Ok!"


def test_bind2():
    args = (5,)
    kwargs = {'c': 2, 'd': 3}
    f1 = bind2(func_math_asorty, *args, **kwargs)
    args = (3,)
    kwargs = {'e': 2, 'f': 3}
    assert f1(*args, **kwargs) == 19

    args = (5, 3, 2)
    f2 = bind2(func_math_asorty, *args)
    kwargs = {'d': 3, 'e': 2, 'f': 3}
    assert f2(**kwargs) == 19

    kwargs = {'a': 5, 'b': 3, 'c': 2}
    f3 = bind2(func_math_asorty, *args)
    kwargs = {'d': 3, 'e': 2, 'f': 3}
    assert f3(**kwargs) == 19

    print "Test bind2 passed Ok!"


def test_bind3():
    assert bind3(f, 1, 2, 3) == [1, 2, 3]
    f2 = bind3(f, 1)
    assert f2(4, 5) == [1, 4, 5]
    assert f2(6, 7) == [1, 6, 7]
    f3 = f2(9)
    assert f3(None) == [1, 9, None]
    assert bind3(f, 1, 2, 3, 4) == [1, 2, 3]
    f4 = bind3(f)
    assert f4(1, 2, 3, 4) == [1, 2, 3]
    assert f4(1, 2, 3) == [1, 2, 3]
    print "Test bind3 passed Ok!"


def main():
    test_map_rek()
    test_filter_rek()
    test_my_reduse()
    test_bind()
    test_bind2()
    test_bind3()


if __name__ == "__main__":
    exit(main())
