from task5_1 import Heron

a, b, c = map(int, input("Введите 3 стороны треугольника: ").split())
if a+b>c and a+c>b and b+c>a:
    Heron(a, b, c)
else:
    print("Решение отсутствует")