import math


def some_func(a, b=9, s="Texting"):
    """
    this func do nothing
    """
    a = a + b
    return a


def func_info(func):
    print func.func_name
    print func.func_code.co_argcount
    print func.func_doc
    print func.func_defaults
    #print %timeit func(10, 15, "First")


def is_positive(num):
    return num >= 0


def my_filter(func, arr):
    rez = []
    for i in arr:
        if func(i):
            rez.append(i)
    return rez


def test_my_filter():
    assert my_filter(is_positive, []) == filter(is_positive, [])
    assert my_filter(is_positive, [3, 0, 5, 7, 8, 1]) == filter(is_positive, [3, 0, 5, 7, 8, 1])
    assert my_filter(is_positive, [-3, -2, -5, -7, -8, -1]) == filter(is_positive, [-3, -2, -5, -7, -8, -1])
    assert my_filter(is_positive, [-3, 0, 5, -7, 8, -1]) == filter(is_positive, [-3, 0, 5, -7, 8, -1])
    assert my_filter(is_positive, [3, 0, "5", 7, 8, 1]) == filter(is_positive, [3, 0, "5", 7, 8, 1])
    print "Ok!"


def mul(a, b):
    return a * b


def my_reduse(func, arr):
    assert len(arr) > 0
    elem = arr[0]
    for i in arr[1:]:
        elem = func(elem, i)
    return elem


def test_my_reduse():
    assert my_reduse(mul, [4]) == reduce(mul, [4])
    assert my_reduse(mul, [2, 3]) == reduce(mul, [2, 3])
    assert my_reduse(mul, [1, 2, 3, 4, 5]) == 2 * 3 * 4 * 5
    assert my_reduse(mul, [0, 3, 4]) == reduce(mul, [0, 3, 4])
    assert my_reduse(mul, [-2, -3, 9]) == reduce(mul, [-2, -3, 9])
    #assert my_reduse(mul, []) == reduce(mul, [])
    print "Ok!"


def haskell_dot(*funcs):
    def fC(x):
        for func in funcs[::-1]:
            x = func(x)
        return x
    return fC


def test_haskell_dot():
    fc = haskell_dot(math.sin, math.cos, math.sqrt)
    assert fc(5) == math.sin(math.cos(math.sqrt(5)))
    print "Ok!"


def main():
    test_my_filter()
    test_my_reduse()
    test_haskell_dot()


main()

"""
def add_some(x):
     def add_closure(val):
         return val + x
     return add_closure

add1 = add_some(1)
add5 = add_some(5)

print add1 is add5
print add1(10)
print add5(10)

import IPython
IPython.embed()
"""
