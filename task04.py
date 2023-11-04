list1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
list2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
list3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

def fix(a):
    a = [x for x in a if x != 2]
    a = [4 if x == 3 else x for x in a]
    return a

print(fix(list1))
print(fix(list2))
print(fix(list3))