class CustomException(Exception):
    pass
def multiply(a,b):
    if b == 0:
        raise CustomException('Ошибка: знаменатель равен 0.')
    return a / b
def pos_subtract(a,b):
    if b > a:
        raise CustomException('Ошибка: результат меньше 0.')
    return a - b
try:
    c = multiply(9, 0)
except CustomException as e:
    print(e)
else:
    print(c)
try:
    c = pos_subtract(1, 2)
except CustomException as e:
    print(e)
else:
    print(c)
try:
    c = pos_subtract(2 ,1)
except CustomException as e:
    print(e)
else:
    print(c)
