import random

def Gamble():
    x = random.randint(1, 6)
    print(x)
    if x == 5 or x == 6:
        print('W')
    elif x == 3 or x == 4:
        Gamble()
    elif x == 1 or x == 2:
        print('L')

if __name__ == '__main__':
    Gamble()
