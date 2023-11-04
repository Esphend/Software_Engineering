from math import sqrt
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
def Square(a, b, c):
    p = (a+b+c)/2
    S = sqrt(p * (p-a) * (p-b) * (p-c))
    return S
print(f"Площадь первого треугольника: {Square(max(one), max(two), max(three))} \n"
      f"Площадь второго треугольника: {Square(min(one), min(two), min(three))}")

