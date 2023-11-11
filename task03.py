def count_digits(string):
    string = list(map(int, string))
    dict = {x: string.count(x) for x in range(10)}
    sorted_digits = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    result = {digit: count for digit, count in sorted_digits[:3]}
    return result

string = input("Введите последовательность чисел: ")
digit_count = count_digits(string)


for digit, count in sorted(digit_count.items()):
    print(f"Число {digit} встречается {count} раз")
