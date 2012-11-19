def set_len(open_sym, end_str):
    lenX = len(end_str)
    return open_sym + str(lenX) + "$" + end_str


def serialize(obj):
    str_rezult = ""
    if isinstance(obj, int):
        str_rezult = "int," + str(obj) + ")"
        str_rezult = set_len("(", str_rezult)
    elif isinstance(obj, str):
        str_rezult = "str," + obj + ")"
        str_rezult = set_len("(", str_rezult)
    elif isinstance(obj, list):
        str1 = ""
        if(len(obj) > 0):
            for item in obj:
                str1 += serialize(item)
                str1 += " "
            str1 = str1[:-1] + "]"
        else:
            str1 = "]"
        str_rezult = set_len("[", str1)

    elif isinstance(obj, dict):
        str1 = ""
        iter_dict = obj.iteritems()
        for item in iter_dict:
            str1 += serialize(item[0])
            str1 += serialize(item[1])
            str1 += " "
        str1 = str1[:-1] + "}"
        str_rezult = set_len("{", str1)

    return str_rezult


def deserialize(in_str):
    assert len(in_str) > 0
    assert in_str[0] == "(" or in_str[0] == "[" or in_str[0] == "{"
    if in_str[0] == "(":
        idx_dol = in_str.find("$")
        assert idx_dol >= 0
        in_str = in_str[idx_dol + 1: -1]
        ind_coma = in_str.find(",")
        type_data = in_str[:ind_coma]
        data = in_str[ind_coma + 1:]
        if type_data == "int":
            return int(data)
        elif type_data == "str":
            return data
    elif in_str[0] == "[":
        result = []
        ########################
        idx_dol = in_str.find("$")
        in_str = in_str[idx_dol + 1:]

        idx_pr = 0
        while idx_pr == 0:
            idx_dol = in_str.find("$")
            assert idx_dol >= 0
            len_var = int(in_str[1: idx_dol])
            result.append(deserialize(in_str[0: idx_dol + len_var + 1]))
            in_str = in_str[idx_dol + len_var + 1:]

            idx_pr = in_str.find(" ")
            if idx_pr == 0:
                in_str = in_str[1:]
        return result

    elif in_str[0] == "{":
        result = {}
        ########################
        idx_dol = in_str.find("$")
        assert idx_dol >= 0
        in_str = in_str[idx_dol + 1:]

        idx_pr = 0
        while idx_pr == 0:

            idx_dol = in_str.find("$")
            assert idx_dol >= 0
            len_var = int(in_str[1: idx_dol])
            key = deserialize(in_str[0: idx_dol + len_var + 1])
            in_str = in_str[idx_dol + len_var + 1:]

            idx_dol = in_str.find("$")
            assert idx_dol >= 0
            len_var = int(in_str[1: idx_dol])
            value = deserialize(in_str[0: idx_dol + len_var + 1])
            in_str = in_str[idx_dol + len_var + 1:]

            idx_pr = in_str.find(" ")
            if idx_pr == 0:
                in_str = in_str[1:]

            result[key] = value

        return result


def test():
    obj = 1
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = "string"
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = [2, "string2"]
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = ["sfg", [2, "string2"]]
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = [[2, "string2"], [3, "string3"]]
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = {4: "string4"}
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = {4: [2, "string2"], 4: "string4"}
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = {4: {4: "string4"}, "strkey1": "string5"}
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = [[1, 3], {1: "tyty"}, {"rrr": "rfrf"}, {9: {"Y": "X"}, 5: ['A', 'B', 'C']}, "sfg"]
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = {'a': 1, 'b': [1, 2, 3, ['3']], 4: 7}
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = ["a n,", "b", "'c'"]
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = ["a n)", "b", "'c'"]
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    obj = [{"()()()":"a n)", 4:"b"}, "'c'"]
    strtest = serialize(obj)
    assert deserialize(strtest) == obj

    print "Test passed OK!"


def main():
    test()


if __name__ == "__main__":
    exit(main())
