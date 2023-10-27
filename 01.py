from datetime import datetime # импорт функции datetime из одноименной библиотеки
from math import sqrt # импорт функции корня из библиотеки math

def main(**kwargs): # определение функции main с использованием параметров "kwargs"
    for key in kwargs.items(): # перебор пар ключ-значение в словаре
        result = sqrt(key[1][2] ** 2 + key[1][1] ** 2) # нахождение квадратного корня
        print(result) #Вывод итогового значения

if __name__ == '__main__': # точка входа
    start_time = datetime.now() # запись текущего времени
    main( # вызов функции main c передачей словаря аргументов
        one = [10, 3],
        two = [5, 4],
        three = [15, 13],
        four = [93, 53],
        five = [133, 15]
    )
    time_costs = datetime.now() - start_time # рассчет времени выполнения
    print(f"Время выполнения программы - {time_costs}") # его последующий вывод
