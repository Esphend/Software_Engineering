def fib(n):
    a, b = 1, 1
    with open("fib.txt", "x") as f:
        for i in range(n):
            yield a
            f.write(f"{a}\n")
            a, b = b, a + b


for num in fib(200):
    print(num)
