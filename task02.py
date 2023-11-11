def tuple_remove(my_tuple, x):
    if x in my_tuple:
        my_tuple.remove(x)
    result_tuple = tuple(my_tuple)
    print(result_tuple)


if __name__ == "__main__":
    a = input("Входные данные: ")
    input_list = []
    for b in a:
        if b.isdigit():
            input_list.append(int(b))
    x = input_list[len(input_list) - 1]
    input_list.pop()
    tuple_remove(input_list, x)
