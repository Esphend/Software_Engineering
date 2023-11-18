bills = int(input("Введите затраты за счета: "))
meals = int(input("Введите затраты на еду: "))
transport = int(input("Введите затраты на транспорт: "))
waste = int(input("Введите непредусмотренные затраты: "))
total = bills+meals+transport+waste

with open("expenses.txt", "x") as file:
    file.write(f"Затраты за счета: {bills} р.\nЗатраты на еду: {meals} р.\n"
               f"Затраты на транспорт: {transport} р.\nНепредусмотренные затраты: {waste} р.\n"
               f"Сумма затрат: {total} р.")
with open("expenses.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        print(line)