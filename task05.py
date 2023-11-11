def revuniq(lst):
    unique = []
    [unique.append(item) for item in reversed(lst) if item not in unique]
    return tuple(unique)

if __name__ == "__main__":
    x = input("Входные данные: ")
    input_list = []
    for k in x:
        if k.isdigit():
            input_list.append(int(k))
    print(revuniq(input_list))