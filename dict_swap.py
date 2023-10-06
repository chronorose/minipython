a = {(1, 2): "a", (3, 4): "a", (5, 6): "a", 5: "a", 4: "a",
     6: "b", 9: "b", 10: "c"}


def dict_swap_2(dict):
    new_dict = {}
    for key, val in dict.items():
        try:
            new_dict[val].append(key)
        except KeyError:
            new_dict[val] = [key]
    for key, val in new_dict.items():
        if len(new_dict[key]) == 1:
            new_dict[key] = val[0]
            continue
        new_dict[key] = tuple(new_dict[key])
    return new_dict


def dict_swap(dict):
    new_dict = {}
    uniq_holder = set()
    for key, val in dict.items():
        if val in uniq_holder:
            new_dict[val] = (new_dict[val], ) + (key, )
            uniq_holder.remove(val)
        elif val in new_dict.keys():
            new_dict[val] = new_dict[val] + (key, )
        else:
            new_dict[val] = key
            uniq_holder.add(val)
    return new_dict


print(dict_swap(a))
print(dict_swap_2(a))
