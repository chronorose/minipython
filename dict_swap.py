a = {(1, 2): "a", (3, 4): "a", (5, 6): "a", 5: "a"}


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
                new_entry = new_entry + (j, )
            new_dict[i] = new_entry
    return new_dict


print(dict_swap(a))

print((1, 2) + (3, 2))
