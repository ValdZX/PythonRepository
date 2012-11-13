def serialize(obj):
    str_rezult = ""
    if isinstance(obj, int):
        str_rezult = "(int," + str(obj) + ")"
    elif isinstance(obj, str):
        str_rezult = "(str," + obj + ")"
    elif isinstance(obj, list):
        str1 = ""
        i = 0
        while i < len(obj) - 1:
            str1 += serialize(obj[i])
            str1 += " "
            i += 1
        str1 += serialize(obj[len(obj) - 1])
        str1 += "]"

        lenX = len(str1)
        str_rezult = "[" + str(lenX) + "$" + str1

    elif isinstance(obj, dict):
        str1 = ""
        ij = 0
        iter_dict = obj.iteritems()
        while ij < (len(obj) - 1):
            item = iter_dict.next()
            str1 += serialize(item[0])
            #str1 += ":"
            str1 += serialize(item[1])
            str1 += " "
            ij += 1
        last_item = iter_dict.next()
        str1 += serialize(last_item[0])
        #str1 += ":"
        str1 += serialize(last_item[1])
        str1 += "}"

        lenX = len(str1)
        str_rezult = "{" + str(lenX) + "$" + str1

    return str_rezult


def deserialize(in_str):
    #if isinstance(in_str, str):
    if in_str[0] == "(":
        tokens = in_str[1:-1].split(",")
        if tokens[0] == "int":
            return int(tokens[1])
        elif tokens[0] == "str":
            return tokens[1]
    elif in_str[0] == "[":
        result = []
        ########################
        idx_tmp = in_str.find("$")
        in_str = in_str[idx_tmp + 1:]

        idx_pr = 0
        while idx_pr == 0:
            if in_str[0] == "[":
                idx_tmp = in_str.find("$")
                len_var = int(in_str[1: idx_tmp])
                result.append(deserialize(in_str[0: idx_tmp + len_var + 1]))
                in_str = in_str[idx_tmp + len_var + 1:]
            elif in_str[0] == "{":
                idx_tmp = in_str.find("$")
                len_var = int(in_str[1: idx_tmp])
                result.append(deserialize(in_str[0: idx_tmp + len_var + 1]))
                in_str = in_str[idx_tmp + len_var + 1:]
            elif in_str[0] == "(":
                idx_end = in_str.find(")")
                result.append(deserialize(in_str[0: idx_end + 1]))
                in_str = in_str[idx_end + 1:]

            idx_pr = in_str.find(" ")
            if idx_pr == 0:
                in_str = in_str[1:]
        return result

    elif in_str[0] == "{":
        result = {}
        ########################
        idx_tmp = in_str.find("$")
        in_str = in_str[idx_tmp + 1:]

        idx_pr = 0
        while idx_pr == 0:
            ind_scob = in_str.find(")")
            key = deserialize(in_str[:ind_scob + 1])
            in_str = in_str[ind_scob + 1:]

            if in_str[0] == "[":
                idx_tmp = in_str.find("$")
                len_var = int(in_str[1: idx_tmp])
                value = deserialize(in_str[0: idx_tmp + len_var + 1])
                in_str = in_str[idx_tmp + len_var + 1:]
            elif in_str[0] == "{":
                idx_tmp = in_str.find("$")
                len_var = int(in_str[1: idx_tmp])
                value = deserialize(in_str[0: idx_tmp + len_var + 1])
                in_str = in_str[idx_tmp + len_var + 1:]
            elif in_str[0] == "(":
                idx_end = in_str.find(")")
                value = deserialize(in_str[0: idx_end + 1])
                in_str = in_str[idx_end + 1:]

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

    print "Test passed OK!"


def main():
    test()


if __name__ == "__main__":
    exit(main())
