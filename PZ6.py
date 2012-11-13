def sum2(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def exrp_calc(arr, dict_func):
    if isinstance(arr[1], tuple):
        a = exrp_calc(arr[1], dict_func)
    else:
        a = arr[1]
    if isinstance(arr[2], tuple):
        b = exrp_calc(arr[2], dict_func)
    else:
        b = arr[2]
    funk = dict_func[arr[0]]
    return funk(a, b)


def test_exrp_calc():
    func_dict = {}
    func_dict['+'] = sum2
    func_dict['-'] = sub
    func_dict['*'] = mul
    func_dict['/'] = div

    print exrp_calc(('+', ('+', 1, 2), ('*', 3, 4)), func_dict)


def compare(filestr1, filestr2):
    result = []
    with open(filestr1, 'rb') as file1:
        with open(filestr2, 'rb') as file2:
            byte1 = file1.read(1)
            byte2 = file2.read(1)
            i = 0
            while byte1 != "":
                if byte1 != byte2:
                    result.append(i)
                byte1 = file1.read(1)
                byte2 = file2.read(1)
                i += 1
    return result


def compare2(filestr1, filestr2):
    result = []
    with open(filestr1, 'r') as file1:
        with open(filestr2, 'r') as file2:
            str1 = file1.read()
            str2 = file2.read()
            result = CompareIter(str1, str2)
    return result


def CompareIter(iter1, iter2):
    result = []
    my_iter1 = iter(iter1)
    my_iter2 = iter(iter2)
    i = 0
    for item1 in my_iter1:
        if item1 != my_iter2.next():
            result.append(i)
        i += 1
    return result


def test_compare():
    print compare("file1.txt", "file2.txt")
    print compare2("file1.txt", "file2.txt")

test_compare()

test_exrp_calc()
