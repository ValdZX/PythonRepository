def mul2(x):
    return x * 2


def map_yield(func, arr):
    it = iter(arr)
    for i in it:
        yield func(i)


def test_map_rek():
    assert map_yield(mul2, (1, 2, 3)) == [2, 4, 6]
    assert map_yield(str, (1, 2, 3)) == ["1", "2", "3"]
    print "Test map_rek passed OK!"


def is_positive(num):
    return num > 0


def my_filter(func, arr):
    it = iter(arr)
    for i in it:
        if func(i):
            yield i


def test_filter_yield():
    gen = my_filter(is_positive, [-1, 5, 6, 0, -3, 4])
    for i in gen:
        print i


def mul(a, b):
    return a * b


def my_reduse(func, arr):
    it = iter(arr)
    elem = it.next()
    for i in it:
        elem = func(elem, i)
        yield elem


def test_reduse_yield():
    gen = my_reduse(mul, my_filter(is_positive, [-1, 5, 6, 0, -3, 4]))
    for i in gen:
        print i


def get_line(fd):
    string = ""
    while True:
        strT = fd.read(1)
        if strT == "":
            break
        if strT == "\n":
            yield string
            string = ""
            continue
        string += strT


def test_get_line():
    with open("test.txt", "w") as input_file:
        input_file.write("put 1\nput 3\nadd\nprint\n")

    with open("test.txt", "r") as input_file:
        gen = get_line(input_file)
        for str1 in gen:
            print str1


def strip_spaces(strings):
    it = iter(strings)
    for i in it:
        yield i.strip(' ')


def test_strip_spaces():
    with open("test.txt", "w") as input_file:
        input_file.write(" put 1 \nput 3 \nadd\n print\n")

    with open("test.txt", "r") as input_file:
        gen = get_line(input_file)
        gen_strip = strip_spaces(gen)
        for i in gen_strip:
            print i


def drop_empty(strings):
    it = iter(strings)
    for i in it:
        if i != "":
            yield i


def test_drop_empty():
    with open("test.txt", "w") as input_file:
        input_file.write(" put 1 \nput 3 \n\n print\n")

    with open("test.txt", "r") as input_file:
        gen = get_line(input_file)
        gen_drop = drop_empty(gen)
        for i in gen_drop:
            print i


def split_items(strings):
    it = iter(strings)
    for i in it:
        for j in i.split():
            yield j


def test_split_items():
    with open("test.txt", "w") as input_file:
        input_file.write(" put 1 \nput 3 \n\n print\n1.5632\n")

    with open("test.txt", "r") as input_file:
        gen = get_line(input_file)
        gen_split = split_items(gen)
        for i in gen_split:
            print i


def get_ints(strings):
    it = iter(strings)
    for i in it:
        x = 0
        try:
            x = int(i)
        except ValueError:
            continue
        yield x


def test_get_ints():
    with open("test.txt", "w") as input_file:
        input_file.write(" put 1 \nput 3 \n\n print\n10\n27\n")

    with open("test.txt", "r") as input_file:
        gen = get_line(input_file)
        gen_ints = get_ints(gen)
        for i in gen_ints:
            print i


def my_sum(strings):
    it = iter(strings)
    elem = it.next()
    for i in it:
        elem += i
        yield elem


def test_my_sum():
    with open("test.txt", "w") as input_file:
        input_file.write(" put 1 \n3\n\n print\n10\n27\n")

    with open("test.txt", "r") as input_file:
        gen = get_line(input_file)
        gen_ints = get_ints(gen)
        gen_sum = my_sum(gen_ints)
        for i in gen_sum:
            print i


def main():
    test_map_rek()
    test_filter_yield()
    test_reduse_yield()

    test_get_line()
    test_strip_spaces()
    test_drop_empty()
    test_split_items()
    test_get_ints()
    test_my_sum()


if __name__ == "__main__":
    exit(main())
