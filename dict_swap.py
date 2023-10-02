a = {"a": 12, "b": 13, "c": 13}


def dict_swap(dict):
    new_dict = {}
    for i in dict.values():
        list = []
        for j in dict.keys():
            if dict[j] == i:
                list.append(j)
        if len(list) == 1:
            new_dict[i] = list[0]
        else:
            new_entry = ()
            for j in list:
                new_entry = new_entry + tuple(j)
            new_dict[i] = new_entry
    return new_dict


print(dict_swap(a))
