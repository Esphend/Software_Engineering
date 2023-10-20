value = 0
pairs = 0
a = []
for i in range(10):
    for j in range(10):
        if i != j:
            value += i
        else:
            pairs += 1
            a.append(i)
print(value)
print(pairs)
print(a)
