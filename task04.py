def cache_result(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items())) #создаем уникальный ключ, на основе функции
        if key in cache: #если ключ кэширован, возвращаем кэшированный результат
            print("From cache: ")
            return cache[key]
        else:
            print("Result: ")
        # если нет, то функция работает как обычно и результат ее работы кэшируется
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper
@cache_result
def multiply(a, b):
    return a * b
@cache_result
def is_even(num):
    return num % 2 == 0
print(multiply(2, 4))
print(multiply(2, 4))
print(is_even(5))
print(is_even(5))
