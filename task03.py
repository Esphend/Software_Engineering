def add_numbers(num):
    try:
        num1 = float(num)
        num2 = 2
        result = num1 + num2
        print("Сумма равна: ", int(result))
    except ValueError:
        print("Введён неверный тип данных. Ожидалось число.")


add_numbers("верный тип данных")
add_numbers(5)