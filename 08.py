value = 0
while 100 - value > value:
        if value == 0:
            value += 10
        elif value % 2 > 0:
            value += 9
        else:
            value += 11
        print(value)