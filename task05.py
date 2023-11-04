import copy

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]


def fix(a):
    b = copy.deepcopy(a)
    res_list = [*set(a)]
    for x in res_list:
        if x in a:
            a.remove(x)
    res_list = [*set(b)]
    for x in a:
        c = x
        while c in res_list:
            c = str(c) + str(x)
        res_list.append(c)
    return set(res_list)

print(fix(list_1))
print(fix(list_2))
print(fix(list_3))
