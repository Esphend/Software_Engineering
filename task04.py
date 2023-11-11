def tuple_slice(input_tuple, id):
    if input_tuple.count(id) >= 2:
        input_tuple = input_tuple[input_tuple.index(id):input_tuple.index(id, 2) + 1]
        print(tuple(input_tuple))
    elif id in input_tuple:
        my_tuple = input_tuple[input_tuple.index(id):len(input_tuple)]
    else:
        print(tuple())


if __name__ == "__main__":
    x = input("Входные данные: ")
    input_list = []
    for k in x:
        if k.isdigit():
            input_list.append(int(k))
    id = input_list[len(input_list) - 1]
    input_list.pop()
    tuple_slice(input_list, id)
