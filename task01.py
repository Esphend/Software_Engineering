import time


def timer(func):
    def stopwatch(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\nНа {func.__name__} ушло {end_time - start_time} сек.")
        return result

    return stopwatch


@timer
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end='')


if __name__ == '__main__':
    fibonacci()
