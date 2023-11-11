num_input = input("Введите числа: ")
num_list = [int(num) for num in num_input.split()]
num_tuple = tuple(num_list)
print(f"Список:{num_list} \nКортеж:{num_tuple}")
